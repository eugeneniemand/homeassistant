using System;
using System.Threading.Tasks;
using System.Reactive.Linq;
using NetDaemon.Common.Reactive;

// Use unique namespaces for your apps if you going to share with others to avoid
// conflicting names
namespace Twinstead
{
    public class Lights : NetDaemonRxApp
    {
        public override void Initialize()
        {
            Entity("binary_sensor.dining").StateChanges
                .Where(e => e.New?.State == "on")
                .Subscribe(e => Entity("light.dining").TurnOn());
        }
    }
}
