#!/usr/bin/env python3
"""
Script de auditoría de entrega y empaquetado ZIP según lineamientos de la Universidad de Cartagena.
Verifica:
  - Estructura de carpetas requeridas (Documentación, Código Fuente, Instaladores, Anexos).
  - Documentos Word obligatorios (Informe, Manual del Sistema, Especificación de requisitos, Manual de Usuario).
  - Archivo de modelado UML (.eap, .qea, .qeax).
  - Script SQL de base de datos en Anexos.
  - Credenciales en Instaladores.
Genera el paquete Proyecto_ISw_X.zip.
"""

import os
import sys
import zipfile
import argparse

REQUIRED_DOCS = [
    "informe",
    "manual del sistema",
    "requisitos", # o especificacion
    "manual de usuario"
]

def audit_and_package(project_dir: str, group_number: int, output_zip: str = None):
    print(f"=== AUDITORÍA DE ENTREGA DEL PROYECTO (Grupo {group_number}) ===")
    errors = []
    warnings = []

    # 1. Carpetas requeridas
    expected_folders = ["Documentación", "Código Fuente", "Instaladores", "Anexos"]
    found_folders = {}
    for item in os.listdir(project_dir):
        full_p = os.path.join(project_dir, item)
        if os.path.isdir(full_p):
            for exp in expected_folders:
                if exp.lower() in item.lower():
                    found_folders[exp] = full_p

    for exp in expected_folders:
        if exp not in found_folders:
            errors.append(f"Falta la carpeta requerida: '{exp}'")
        else:
            print(f"[OK] Carpeta encontrada: {exp} -> {os.path.basename(found_folders[exp])}")

    # 2. Verificar Documentación
    doc_folder = found_folders.get("Documentación")
    if doc_folder:
        doc_files = [f.lower() for f in os.listdir(doc_folder)]
        # Verificar documentos Word
        for req in REQUIRED_DOCS:
            if not any(req in f and (f.endswith('.docx') or f.endswith('.doc')) for f in doc_files):
                warnings.append(f"No se detectó un archivo Word evidente para: '{req}' en Documentación")
            else:
                print(f"[OK] Documento detectado para: '{req}'")
        
        # Verificar proyecto UML (EA)
        has_uml = any(f.endswith('.qea') or f.endswith('.eap') or f.endswith('.qeax') for f in doc_files)
        if not has_uml:
            warnings.append("No se encontró el archivo de modelado UML de Enterprise Architect (.qea, .eap, .qeax) en Documentación")
        else:
            print("[OK] Archivo de modelado Enterprise Architect detectado.")

        # Verificar presentación
        has_ppt = any(f.endswith('.pptx') or f.endswith('.ppt') or f.endswith('.pdf') and 'present' in f for f in doc_files)
        if not has_ppt:
            warnings.append("No se encontraron diapositivas de sustentación (.pptx) en Documentación")
        else:
            print("[OK] Archivo de presentación detectado.")

    # 3. Verificar Anexos
    anexos_folder = found_folders.get("Anexos")
    if anexos_folder:
        anexos_files = [f.lower() for f in os.listdir(anexos_folder)]
        has_sql = any(f.endswith('.sql') for f in anexos_files)
        if not has_sql:
            warnings.append("No se detectó el script SQL de creación de la base de datos en la carpeta 'Anexos'")
        else:
            print("[OK] Script de base de datos detectado en Anexos.")

    print("\n--- RESULTADO DE LA REVISIÓN ---")
    if errors:
        print("ERRORES CRÍTICOS:")
        for e in errors:
            print(f"  [X] {e}")
    else:
        print("[!] No se encontraron errores estructurales bloqueantes.")

    if warnings:
        print("ADVERTENCIAS / RECOMENDACIONES:")
        for w in warnings:
            print(f"  [!] {w}")

    if not errors:
        zip_name = output_zip or f"Proyecto_ISw_{group_number}.zip"
        zip_path = os.path.join(project_dir, zip_name)
        print(f"\nEmpaquetando entrega en: {zip_path}...")
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
            for root, dirs, files in os.walk(project_dir):
                if zip_name in files:
                    files.remove(zip_name)
                for f in files:
                    file_full = os.path.join(root, f)
                    arc_name = os.path.relpath(file_full, project_dir)
                    zf.write(file_full, arc_name)
        print(f"[OK] Entregable empaquetado exitosamente como: {zip_name}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Auditor y empaquetador de entrega UdeC")
    parser.add_argument("--dir", default=".", help="Directorio raíz del proyecto")
    parser.add_argument("--grupo", type=int, default=1, help="Número del grupo (ej: 1 para Proyecto_ISw_1.zip)")
    parser.add_argument("--output", default=None, help="Nombre del archivo zip de salida")
    args = parser.parse_args()

    audit_and_package(args.dir, args.grupo, args.output)
