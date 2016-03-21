import subprocess

def add_netns_segment(powerline):
    try:
        env = subprocess.check_output(['ip', 'netns', 'identify'], stderr=subprocess.STDOUT).rstrip()
    except Exception, e:    
        env = str(e.output)

    if not bool(env.strip()):
        return

    env_name = os.path.basename(env)
    bg = Color.VIRTUAL_ENV_BG
    fg = Color.VIRTUAL_ENV_FG
    powerline.append('NS: %s ' % env_name, fg, bg)

