import azure.functions as func
import logging
import json

app = func.FunctionApp()

@app.function_name(name="FunctionForAPIChunk28494")
@app.cosmos_db_input(
    arg_name="currentNumber",  # Renamed for consistency
    database_name="VisitorCountDatabase",
    container_name="SiteVisitors",
    connection="CosmosDbConnectionSetting",
    id="global_visitor_count",  # Matches document ID
    partition_key="main_site"   # Matches partition key value in the document
)
@app.cosmos_db_output(
    arg_name="updatedNumber",  # Renamed to avoid underscores
    database_name="VisitorCountDatabase",
    container_name="SiteVisitors",
    connection="CosmosDbConnectionSetting"
)
@app.route(route="updatecounter/global_visitor_count")
def update_counter(
    req: func.HttpRequest,
    currentNumber: func.DocumentList,  # Matches the input binding name
    updatedNumber: func.Out[func.Document]  # Matches the output binding name
) -> func.HttpResponse:
    if not currentNumber or len(currentNumber) == 0:
        return func.HttpResponse("Current visitor number not found.", status_code=404)

    # Convert Document to a dictionary
    doc_dict = json.loads(currentNumber[0].to_json())

    # Increment the 'visitCount' field
    doc_dict["visitCount"] = doc_dict.get("visitCount", 0) + 1

    # Save the updated number back to Cosmos DB as a Document
    updatedNumber.set(func.Document.from_json(json.dumps(doc_dict)))

    # Log the updated document
    logging.info(f"Updated document: {doc_dict}")

    return func.HttpResponse(json.dumps(doc_dict), status_code=200, mimetype="application/json")