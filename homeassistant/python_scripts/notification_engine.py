#params = data.get("params")
def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

lights = hass.states.entity_ids("light")
hasNumbers("abc3bbb")
#filtered_lights = [light for light in lights if hasNumbers(light)]

logger.warning(filtered_lights)