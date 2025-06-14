// __tests__/addProduct.test.js
import { handler } from '../path/to/your/addProduct';
import { mockClient } from 'aws-sdk-client-mock';
import { PutCommand } from "@aws-sdk/lib-dynamodb";
import { DynamoDBDocumentClient } from "@aws-sdk/lib-dynamodb";

const ddbMock = mockClient(DynamoDBDocumentClient);

beforeEach(() => ddbMock.reset());

describe('addProduct handler', () => {
  test('✅ Erfolgreiches Hinzufügen eines Produkts', async () => {
    ddbMock.on(PutCommand).resolves({});

    const event = {
      body: JSON.stringify({
        name: "USB-Kabel",
        category: "Zubehör",
        quantity: 100,
        location: "Regal A3"
      })
    };

    const result = await handler(event);
    const body = JSON.parse(result.body);

    expect(result.statusCode).toBe(201);
    expect(body.message).toBe("Produkt hinzugefügt.");
    expect(body.product).toHaveProperty("id");
    expect(body.product.id).toMatch(/^prod-\d+$/);
    expect(new Date(body.product.createdAt).toISOString()).toBe(body.product.createdAt);
  });

  test('❌ Fehlende Pflichtfelder', async () => {
    const event = {
      body: JSON.stringify({
        name: "",
        category: "Zubehör",
        quantity: 100
      })
    };

    const result = await handler(event);
    const body = JSON.parse(result.body);

    expect(result.statusCode).toBe(400);
    expect(body.message).toBe("Fehlende Produktinformationen.");
  });

  test('🔥 Fehler bei DynamoDB-Operation', async () => {
    ddbMock.on(PutCommand).rejects(new Error("DynamoDB-Zugriffsfehler"));

    const event = {
      body: JSON.stringify({
        name: "Adapter",
        category: "Technik",
        quantity: 50,
        location: "Regal B2"
      })
    };

    const result = await handler(event);
    const body = JSON.parse(result.body);

    expect(result.statusCode).toBe(500);
    expect(body.error).toMatch(/DynamoDB-Zugriffsfehler/);
  });
});
