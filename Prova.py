import rclpy
from geometry_msgs.msg import Twist
from rclpy.node import Node
import time
from collections import deque

#Tem algum problema seja no Vs code ou na minha máquina, não consigo importar por nada essas 2 bibliotécas então vou ter que fazer sem testar nada. 
#Não usei o argparse pq não entendi nada de como usa-lo
import typer
import inquirer

app = typer.Typer()
dq = deque()

class PublisherController(Node):
    def __init__(self):
        super().__init__('publisher_controller')
        self.publisher = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)

    def turtle_move(self, linear_speed, angular_speed, duration):
        msg = Twist()
        msg.linear.x = linear_speed
        msg.angular.z = angular_speed 

        start_time = time.time()

        while time.time() - start_time < duration:
            self.publisher.publish(msg)
            self.get_logger().info('Movimento enviado: linear=%f, angular=%f' % (linear_speed, angular_speed))
            time.sleep(0.1)

        dq.popleft


@app.command()
def mover_robo(vx:float, vy:float, vtheta:float, t:int):
    if ((vx >= 0) and (vy>= 0)  and (vtheta >= 0)  and (t >= 0)):
        dq.append(vx,vy,vtheta,t)


def CLI:
    questions = [inquirer.Text(xv="xv" message="xv:"),
                 inquirer.Text(xy="xy" message="xy:"),
                 inquirer.Text(xtheta="xtheta" message="xtheta:"),
                 inquirer.Text(t="t" message="t:")]
    
    answers = inquirer.prompt(questions)
    #como não consigo testar não sei a saida desse answers e por tanto não sei como ligar no mover_robo do typer.

def read_deque():
    PublisherController.turtle_move(dq[1])
    # Não sei implentar essa lógica direito

#Enfim foi isso, não consegui fazer praticamente nada, mas tentei muito e to a 1 passo de ficar maluco se tentar mais um pouco...
#Obrigado pela atenção.
    