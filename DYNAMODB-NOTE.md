# DynamoDB policy in the original notes

The source PDF contains an IAM policy granting DynamoDB read/write permissions with the placeholder `YOUR-TABLE-ARN`. **The Lambda code documented in the PDF does not call DynamoDB**: it calculates a power and returns a JSON response. Therefore the deployed app's data persistence cannot be confirmed from the supplied code.

`dynamodb-policy-from-notes.json` is included as a record of the learning exercise, **not as a deployable or required policy**. Do not grant these permissions to the current calculation-only Lambda. If adding persistence later, provision a table and narrow the role to the exact actions and table ARN the implementation needs. Do not leave `YOUR-TABLE-ARN` as-is.
