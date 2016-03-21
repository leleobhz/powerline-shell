import subprocess

def add_netns_segment(powerline):
    env = subprocess.check_output(['ip', 'netns', 'identify', "$$"], stderr=subprocess.STDOUT)
    if env is None:
        return

    env_name = os.path.basename(env)
    bg = Color.VIRTUAL_ENV_BG
    fg = Color.VIRTUAL_ENV_FG
    powerline.append(' %s ' % env_name, fg, bg)
