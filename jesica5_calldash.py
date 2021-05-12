from jesica4 import create_dashboard
from jesica4 import command_light
from jesica4 import command_SoundSystem
from jesica4 import command_Door
from jesica4 import command_detectsound

command_light(True, '#FFC200', 'Turn on the light Jeffrey to yellow')
command_SoundSystem('On', 30, 'Can you turn on the speakers to 30%')
command_Door('Open', 'Please open the door')
command_detectsound('dog_bark')
app = create_dashboard()
app.run_server(debug=True)