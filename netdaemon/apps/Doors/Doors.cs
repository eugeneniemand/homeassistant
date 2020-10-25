using System;
using System.Threading.Tasks;
using System.Reactive.Linq;
using NetDaemon.Common.Reactive;

// Use unique namespaces for your apps if you going to share with others to avoid
// conflicting names
namespace Twinstead
{
    public class Doors : NetDaemonRxApp
    {
        public override void Initialize()
        {
            Log("Door Init");
        }

        public string Test = "SomeString";
    }
}
