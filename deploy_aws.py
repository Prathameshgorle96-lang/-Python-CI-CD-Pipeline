"""
deploy_aws.py — Deployment script called by GitHub Actions after tests pass.
Packages and updates the Lambda function (or prints success if no Lambda configured).
"""

import boto3
import zipfile
import os
import json

FUNCTION_NAME = os.environ.get("LAMBDA_FUNCTION_NAME", "")
REGION = os.environ.get("AWS_REGION", "us-east-1")


def zip_app():
    zip_path = "/tmp/app.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for root, dirs, files in os.walk("app"):
            for file in files:
                path = os.path.join(root, file)
                z.write(path)
    return zip_path


def deploy():
    if not FUNCTION_NAME:
        print("No LAMBDA_FUNCTION_NAME set — skipping Lambda update.")
        print("Deployment step complete (dry run).")
        return

    print(f"Updating Lambda function: {FUNCTION_NAME}")
    lam = boto3.client("lambda", region_name=REGION)
    zip_path = zip_app()
    with open(zip_path, "rb") as f:
        code = f.read()
    response = lam.update_function_code(FunctionName=FUNCTION_NAME, ZipFile=code)
    print(f"Updated: {response['FunctionName']} — version {response.get('Version', 'latest')}")
    print("Deployment successful.")


if __name__ == "__main__":
    deploy()
