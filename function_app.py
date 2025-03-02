import azure.functions as func
import logging

app = func.FunctionApp()

@app.blob_trigger(arg_name="myblob", path="disrupt-aec-container/*.jpg",
                               connection="disruptaec_STORAGE") 
def trigger_model(myblob: func.InputStream):
    logging.info(f"Python blob trigger function processed blob"
                f"Name: {myblob.name}"
                f"Blob Size: {myblob.length} bytes")
    
    blob_content = myblob.read()
    logging.info("blob content successfully read")

