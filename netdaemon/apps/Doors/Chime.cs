using System;
using System.Threading.Tasks;
using System.Reactive.Linq;
using NetDaemon.Common.Reactive;

// Use unique namespaces for your apps if you going to share with others to avoid
// conflicting names
namespace Twinstead
{
    public class Chime : NetDaemonRxApp
    {

        public override void Initialize()
        {
            Log("Door Chimes Init");
            var doorsMain = GetApp("doors_main");
            Log(doorsMain.Test);
            Entity("binary_sensor.front_door").StateChanges
                .Where(e => e.New?.State == "on")
                .Subscribe(e => {
                    Entity("switch.alarm_beep_two").TurnOn();
                    Log("Front Door Beep");
                    }
                );

            Entity("binary_sensor.back_door").StateChanges
                .Where(e => e.New?.State == "on")
                .Subscribe(e => Entity("switch.alarm_beep_three").TurnOn());


        }
    }
}
