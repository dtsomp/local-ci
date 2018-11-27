#!/usr/bin/env python3.5

#import yaml,os
import yaml,subprocess,sys

my_stage = 'test'
        
def print_stages(data):
    print("Stages: [%s]" % ', '.join(map(str,data['stages'])))

def get_steps(data, stage):
    steps = []
    if stage in data['stages']:
        for entry in data:
            if 'stage' in data[entry] and data[entry]['stage'] == stage:
                steps.append(entry)
    return steps

def run_step(step):
    #    os.system('gitlab-runner exec docker "%s"' % step)
    return subprocess.run(['gitlab-runner', "exec", "docker", "%s" % step])


## Main


with open('.gitlab-ci.yml') as f:
    dataMap = yaml.safe_load(f)

    if len(sys.argv) == 1:
        print( "You need to provide at least one CI step")
        print_stages(dataMap)
        sys.exit(1)

    for stage in sys.argv[1:]:
        print(stage)
        if stage not in dataMap['stages']:
            print("No stage named " + stage + " was found")
            print_stages(dataMap)
            sys.exit(1)


        for step in get_steps(dataMap, stage):
            print('\033[95mJob name: ' + step + '\033[0m\n')
            
            res = run_step(step)
            print('\n\033[95m' + step + ' exited with returncode: ' + str(res.returncode) + '\033[0m\n')
            if res.returncode != 0:
                print('\n\033[91mJob failed!\033[0m')
                sys.exit(res.returncode)

   

