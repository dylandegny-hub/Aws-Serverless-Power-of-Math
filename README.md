# Power of Math | AWS Serverless Web App

A hands-on **guided AWS project** demonstrating how to host a browser-based calculator and connect it to a serverless Python backend through a REST API.

The app accepts a **base** and an **exponent**, invokes an AWS Lambda function through Amazon API Gateway, and displays the calculation in the browser. Example from my deployment: **2⁸ = 256**.

**Live demo (recorded deployment):** https://staging.dpeqe5botwvc6.amplifyapp.com/  
*Availability may change when AWS resources are updated or removed. This link has not been independently live-tested for this repository.*

![Successful computation of 2 to the eighth power](assets/power-of-math-success.png)

## Architecture

```mermaid
flowchart LR
    U[User browser] --> A[AWS Amplify Hosting / index.html]
    A -->|HTTPS POST with JSON| G[Amazon API Gateway]
    G --> L[AWS Lambda / Python]
    L -->|JSON result| G
    G -->|Response| A
    L -.-> I[IAM execution role]
```

### Tech stack

| Component | Purpose |
| --- | --- |
| HTML, CSS, JavaScript | Calculator interface and `fetch()` call |
| AWS Amplify Hosting | Host and deploy static website files |
| Amazon API Gateway | Public REST endpoint accepting POST requests |
| AWS Lambda (Python) | Parse JSON and compute exponentiation with `math.pow()` |
| AWS IAM | Execution role and service permissions |
| Amazon DynamoDB | **Documented as a potential extension; not used in the Lambda code included here** |

## How it works

1. Enter the base and exponent in the hosted HTML page.
2. JavaScript sends JSON of the form `{"base":"2","exponent":"8"}` to the API Gateway `POST` endpoint.
3. API Gateway invokes the Python Lambda function with the request body.
4. Lambda converts the inputs to integers, computes `math.pow(base, exponent)`, and returns a JSON number.
5. JavaScript displays the result in a browser alert.

## Repository structure

```text
aws-serverless-power-of-math/
├── index.html                          # Static frontend (at ZIP root for Amplify)
├── lambda/
│   └── lambda_function.py             # Python Lambda handler
├── assets/
│   └── power-of-math-success.png      # Screenshot from my actual deployment
├── docs/
│   ├── DYNAMODB-NOTE.md               # Clarifies DynamoDB is not implemented
│   └── dynamodb-policy-from-notes.json
├── tests/
│   └── test_lambda.py                 # Local standard-library unit tests
├── .gitignore
└── README.md
```

## Deploy your own version

**Prerequisites:** An AWS account with permission to create Lambda, API Gateway and Amplify resources, and a browser or local text editor.

1. Create a Python Lambda function and paste the contents of [`lambda/lambda_function.py`](lambda/lambda_function.py) into its code editor. The handler should be `lambda_function.lambda_handler`.
2. Create an API Gateway endpoint integrated with the Lambda function. Configure a **POST** method with Lambda proxy integration, and enable CORS for the origin of your Amplify site (or `*` for a public learning demo). Deploy your API stage.
3. Replace the API Gateway URL in [`index.html`](index.html) with your API's invoke URL. The example URL in this repository comes from my own recorded deployment.
4. To deploy manually with Amplify Hosting, select **the `index.html` file itself**, zip it into a deployment archive, and upload that ZIP. **`index.html` must be at the root of the ZIP**, not inside a `website/` or `index2/` directory. The separate `amplify-upload.zip` included in the downloads is already correctly structured.
5. Enter `2` and `8` and press **CALCULATE**. The expected result is `256` (or `256.0`, depending on response formatting).

To test the Lambda handler locally without an AWS account:

```sh
python -m unittest discover -s tests -v
```

> **Cloud cost reminder:** API Gateway and Lambda may incur charges outside free tier limits. The example endpoint is public, so consider API throttling, monitoring, and additional controls before sustained public use.

## What I learned

- Connecting a static website to AWS serverless backend services.
- Passing and parsing JSON through a REST-style API integration.
- Setting up Lambda execution permissions and troubleshooting cross-origin requests.
- Deploying the exact contents required by AWS Amplify, including resolving ZIP-root structure issues.
- Validating an end-to-end calculation through the hosted application.

## Potential improvements

- Add input validation and user-friendly API errors (the tutorial version returns HTTP 500 even for invalid input).
- Use a more robust request/response UI instead of browser `alert()`.
- Add DynamoDB persistence only after implementing actual table writes and least-privilege permissions.
- Add CloudWatch monitoring and API Gateway throttling to control cost and abuse.
- Support more input types with deliberate precision/overflow handling (`math.pow()` currently returns a float).

## Credits

This was a **learning project**, built and documented, which covers AWS Amplify, API Gateway, Lambda, IAM and DynamoDB. I reproduced the core app to practice deployment and service integration; the screenshots show my own implementation and successful test. The full DynamoDB write step is not demonstrated in the Lambda source preserved in my notes.
