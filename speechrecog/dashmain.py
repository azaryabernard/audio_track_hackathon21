
from jesica4 import create_dashboard
from jesica4 import command_light
from jesica4 import command_SoundSystem
from jesica4 import command_Door
from jesica4 import command_detectsound


app = create_dashboard()
app.run_server(debug=False)