import logging
import azure.functions as func

#app = func.FunctionApp(http_auth_level=func.AuthLevel.Anonymous)
app = func.FunctionApp()

@app.function_name(name="eventhub_output")
@app.route(route="eventhub_output", auth_level=func.AuthLevel.ANONYMOUS)
@app.event_hub_output(arg_name="event",
                      event_hub_name="matteh56",
                      connection="ehconnstring")
def eventhub_output(req: func.HttpRequest, event: func.Out[str]):
    body = req.get_body()
    if body is not None:
        event.set(body.decode('utf-8'))
    else:    
        logging.info('req body is none')
    return 'ok'
