# Power Apps / Power Automate connector for Function App

Use this document as the connector definition to call a secured Azure Function from Power Apps or Power Automate. Replace the placeholders (YOUR-...) with your tenant, app registration, and function app values before importing.

Example connector JSON (replace placeholders):

```json
{
  "name": "FunctionAppConnector",
  "properties": {
    "displayName": "Function App Connector",
    "description": "Call the secured Azure Function from Power Apps / Power Automate",
    "iconBrandColor": "#0078D4",
    "capabilities": [
      "actions"
    ],
    "connectionParameters": {
      "token": {
        "type": "oauthSetting",
        "oAuthSettings": {
          "identityProvider": "aad", 
          "clientId": "YOUR-API-APP-REG-CLIENT-ID",
          "scopes": [
            "api://YOUR-API-APP-REG-CLIENT-ID/.default"
          ],
          "redirectMode": "Global",
          "redirectUrl": "https://global.consent.azure-apim.net/redirect",
          "properties": {
            "IsFirstParty": "False",
            "AzureActiveDirectoryResourceId": "api://YOUR-API-APP-REG-CLIENT-ID",
            "TenantId": "YOUR-TENANT-ID"
          },
          "customParameters": {
            "resourceUri": {
              "value": "api://YOUR-API-APP-REG-CLIENT-ID"
            },
            "loginUri": {
              "value": "https://login.microsoftonline.com"
            },
            "tenantId": {
              "value": "YOUR-TENANT-ID"
            }
          }
        }
      }
    },
    "publisher": "Your Team",
    "backendService": {
      "serviceUrl": "https://YOUR-FUNCTION-APP.azurewebsites.net"
    },
    "schemaVersion": "2016-10-24",
    "actions": {
      "ProcessData": {
        "type": "object",
        "displayName": "Process Data",
        "description": "Send data to the Function for processing",
        "operationId": "ProcessData",
        "visibility": "important",
        "inputs": {
          "method": "post",
          "path": "/api/process-data",
          "authentication": {
            "type": "Raw",
            "value": "Bearer @{connectionParameters('token')}"
          },
          "headers": {
            "Content-Type": "application/json"
          },
          "body": {
            "type": "object",
            "required": [
              "fileName",
              "content"
            ],
            "properties": {
              "fileName": {
                "type": "string",
                "description": "Original file name"
              },
              "content": {
                "type": "string",
                "description": "Payload to process, base64 or JSON string"
              }
            }
          }
        },
        "outputs": {
          "statusCodes": [
            200,
            400,
            401,
            500
          ],
          "body": {
            "type": "object",
            "properties": {
              "status": {
                "type": "string",
                "description": "Result status"
              },
              "message": {
                "type": "string",
                "description": "Details from the function"
              },
              "result": {
                "type": "object",
                "description": "Processed result payload"
              }
            }
          }
        }
      }
    }
  }
}
```

How to use

- Replace the placeholders in the JSON with your tenant and app registration values.
- Ensure your Function App is protected by Azure AD (EasyAuth or a validated bearer token in-code).
- Import the JSON as a custom connector in Power Apps / Power Automate and configure the AAD settings.

Example request body:

```json
{
  "fileName": "example.txt",
  "content": "SGVsbG8gV29ybGQh"
}
```

Expected example response (from the sample handler):

```json
{
  "status": "success",
  "result": {
    "input": {
      "fileName": "example.txt",
      "content": "SGVsbG8gV29ybGQh"
    },
    "length": 2
  }
}
```

Security note: keep client ids and secrets safe; prefer certificate auth for production.
