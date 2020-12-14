from robot_chat_client import RobotChatClient
from flask_ask import Ask, statement
import time
import driver
//run this program whenever in command window whenever you want the robots to dance over cloud
def test_callback(message_dict):
    print('Received dictionary {}'.format(message_dict))
    print('The message is type {}'.format(message_dict['type']))

    if message_dict['type'] == 'test_message_type': 
        print('Value of field foo: {}'.format(message_dict['foo']))

    if message_dict['type'] == 'users': 
        print('Number of users: {}'.format(message_dict['count']))

    if message_dict['type'] == 'dance': //dance case runs through thread
      print('Party Time') 
      driver.event.clear()
      driver_thread= threading.Thread(target=driver.dance)
      driver_thread.start()
      speech_text = 'Party time'
      return statement(speech_text).simple_card('Johnny', speech_text) 

    
# Run this script directly to invoke this test sequence
if __name__ == '__main__':
    print('Creating RobotChatClient object')
    client = RobotChatClient('ws://localhost:5001', callback=test_callback) //change this to the aws server ip

    time.sleep(1)
    print('Sending a dance message')  //this part sends the dance message into the server
    client.send({'dance'})

    print('Waiting for ctrl+c')
