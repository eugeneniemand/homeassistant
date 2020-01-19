entities = data.get("entity_id")
for entity_id in entities:
    entity_name = entity_id.split(".")[1]
    timeout = hass.states.get("input_number."+ entity_name +"_timeout").state
    service_data = {"entity_id": entity_id, "duration": (f"00:{int(float(timeout)):02}:00")}
    logger.warning(service_data)
    hass.services.call("timer", "start", service_data, False)