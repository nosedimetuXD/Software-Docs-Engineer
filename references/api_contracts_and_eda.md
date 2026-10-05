# API Contracts Specification: Synchronous & Asynchronous

In modern distributed software, APIs define boundary contracts between independent systems. Accurate, machine-verifiable documentation is critical to developer experience and automated client generation.

---

## 1. Synchronous Contracts (OpenAPI 3.1)

### Key Capabilities in OpenAPI 3.1:
- **Full JSON Schema 2020-12 alignment:** Permits modern schema keywords (`prefixItems`, `unevaluatedProperties`, `$dynamicAnchor`, `contains`).
- **Webhooks support:** Define asynchronous callbacks and outbound HTTP notifications in the root `webhooks` object.
- **RFC 7807 / RFC 9457 (Problem Details):** Standardize all error responses (4xx and 5xx) with `application/problem+json`.

### Anatomy of an OpenAPI 3.1 Endpoint

```yaml
openapi: 3.1.0
info:
  title: Order Processing Service
  version: 1.2.0
  description: High-throughput order management API.
paths:
  /v1/orders/{orderId}:
    get:
      summary: Fetch order details
      operationId: getOrderById
      parameters:
        - name: orderId
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Order found successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Order'
        '404':
          description: Order not found
          content:
            application/problem+json:
              schema:
                $ref: '#/components/schemas/ProblemDetails'
components:
  schemas:
    Order:
      type: object
      required: [id, amount, status, createdAt]
      properties:
        id:
          type: string
          format: uuid
        amount:
          type: number
          minimum: 0.01
        status:
          type: string
          enum: [PENDING, PAID, SHIPPED, CANCELLED]
        createdAt:
          type: string
          format: date-time
    ProblemDetails:
      type: object
      required: [type, title, status]
      properties:
        type:
          type: string
          format: uri
        title:
          type: string
        status:
          type: integer
        detail:
          type: string
```

---

## 2. Asynchronous Contracts (AsyncAPI 3.0)

When APIs communicate over message brokers (Apache Kafka, RabbitMQ, MQTT, WebSockets), traditional request-reply schemas fail to model broker topologies. AsyncAPI 3.0 cleanly decouples **Channels** from **Operations**.

### Key Concepts:
- **Channels:** Where events travel (Kafka topics, AMQP queues, MQTT paths).
- **Operations:** What a service does on a channel:
  - `action: receive` (the service consumes messages from the channel).
  - `action: send` (the service publishes messages to the channel).
- **Messages:** The payload schema, headers, and encoding (JSON Schema, Avro, Protobuf).

### AsyncAPI 3.0 Example

```yaml
asyncapi: 3.0.0
info:
  title: Order Events Stream
  version: 1.0.0
channels:
  orderEvents:
    address: orders.v1.events
    messages:
      OrderCreated:
        $ref: '#/components/messages/OrderCreated'
operations:
  onOrderCreated:
    action: receive
    channel:
      $ref: '#/channels/orderEvents'
    summary: Service consumes order creation events for fulfillment.
components:
  messages:
    OrderCreated:
      payload:
        type: object
        required: [orderId, customerId, timestamp]
        properties:
          orderId:
            type: string
            format: uuid
          customerId:
            type: string
          timestamp:
            type: string
            format: date-time
```

---

## 3. Breaking Change Detection & Governance

Never deploy API contract changes without checking for backward compatibility. Use automated tools in CI/CD:
- **Linting:** Use `Spectral` to enforce corporate style guides and complete documentation on every operation.
- **Schema Diffing:** Use tools like `oasdiff` or `openapi-diff` to block PRs introducing breaking changes (e.g., removing an enum value, making an optional parameter required, changing response types).
