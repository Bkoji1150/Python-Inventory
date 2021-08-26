import shlex, subprocess
cmd="dir"
sp=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rc=sp.wait()
out,err=sp.communicate()
print(f'OUTPUT IS:\n {out}')
print(f'Error is:\n {err}')
