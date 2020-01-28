import utils

def get_on_lights(lights):
    lights = { k: lights[k] for k in lights.keys() if not utils.hasNumbers(k) and lights[k]["state"] == "on"}
    return [light.replace("light.","") for light in lights.keys()]

def get_idle_timers(timers):
    timers = { k: timers[k] for k in timers.keys() if timers[k]["state"] == "idle"}
    return [timer.replace("timer.","") for timer in timers.keys()]

def get_lights_without_timers(lights, timers):
    l = get_on_lights(lights)
    t = get_idle_timers(timers)
    return utils.intersect(l,t)

def build_message(messageType, light_states, timer_states):
    if messageType != "LightsInfo" and messageType != "LightsCount":
        return ""

    lights_without_timers = get_lights_without_timers(light_states,timer_states)
    number_of_lights = len(lights_without_timers)

    if messageType == "LightsInfo" and number_of_lights > 0:           
        return ", ".join(lights_without_timers)       
    
    if messageType == "LightsCount" and number_of_lights > 0: 
        return f"{number_of_lights} lights on" if number_of_lights > 1 else "1 light on"
    
    return ""
