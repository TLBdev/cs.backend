# Generated by Django 3.0.5 on 2020-04-28 20:45

from django.db import migrations
from ..models import Room

def connectRooms(object, destinationRoom, direction):
    
    destinationRoomID = destinationRoom.id
    try:
      destinationRoom = Room.objects.get(id=destinationRoomID)
    except Room.DoesNotExist:
      print("That room does not exist")
    else:
      if direction == "up":
        object.up_id = destinationRoomID
      elif direction == "down":
        object.down_id = destinationRoomID
      elif direction == "left":
        object.left_id = destinationRoomID
      elif direction == "right":
        object.right_id = destinationRoomID
      elif direction == "inside":
        object.inside_id = destinationRoomID
      elif direction == "outside":
        object.outside_id = destinationRoomID
      else:
        print("Invalid direction")
        return
      object.save()

def seed_everything(apps, schema_editor):
    Room = apps.get_model('main', 'Room')
    Season = apps.get_model('main', 'Season')
    Items = apps.get_model('main', 'Items')
    room_names = [
        ['Dec20-26','Jan1-4','Jan5-11','Jan12-18','Jan19-25','Jan/Feb26-1','Feb2-8','Feb9-15','Feb16-22','Feb23-29','Mar1-7','Mar8-14','Mar15-21'],
        ['Mar22-28', 'Mar/Apr29-4', 'Apr5-11', 'Apr12-18', 'Apr19-25', 'Apr/May26-2', 'May3-9', 'May10-16', 'May17-23', 'May24-30', 'May/Jun31-6', 'Jun7-13', 'Jun14-20'],
        ['Jun21-27', 'Jun28-Jul4', 'Jul5-11', 'Jul12-18', 'Jul19-25', 'Jul26-Aug1', 'Aug2-8', 'Aug9-15', 'Aug16-22', 'Aug23-29', 'Aug30-Sept5', 'Sept6-12', 'Sept13-19'],
        ['Sept20-26', 'Sept27-Oct3', 'Oct4-10', 'Oct11-17', 'Oct18-24', 'Oct25-31', 'Nov1-7', 'Nov8-14', 'Nov15-21', 'Nov22-28', 'Nov29-Dec5', 'Dec6-12', 'Dec13-19']
    ]
    rooms=[]
    rooms_outside=[]
    for season in range(len(room_names)):
        for week in range(len(room_names[season])):
            room = Room(name=room_names[season][week], season_id=season+1)
            room.save()
            rooms.append(room)
    
    for season in range(len(room_names)):
        for week in range(len(room_names[season])):
            room = Room(name=f'{room_names[season][week]}-outside', season_id=season+1)
            room.save()
            rooms_outside.append(room)

    for i in range(len(rooms)):
        connectRooms(rooms[i], rooms_outside[i], 'outside')
        connectRooms(rooms_outside[i], rooms[i], 'inside')

    rooms2d = []
    rooms2d.append(rooms[:4])
    rooms2d.append(rooms[4:8])
    rooms2d.append(rooms[8:12])
    rooms2d.append(rooms[12:16])
    rooms2d.append(rooms[16:20])
    rooms2d.append(rooms[20:24])
    rooms2d.append(rooms[24:28])
    rooms2d.append(rooms[28:32])
    rooms2d.append(rooms[32:36])
    rooms2d.append(rooms[36:40])
    rooms2d.append(rooms[40:44])
    rooms2d.append(rooms[44:48])
    rooms2d.append(rooms[48:])

    rooms2d_outside = []
    rooms2d_outside.append(rooms_outside[:4])
    rooms2d_outside.append(rooms_outside[4:8])
    rooms2d_outside.append(rooms_outside[8:12])
    rooms2d_outside.append(rooms_outside[12:16])
    rooms2d_outside.append(rooms_outside[16:20])
    rooms2d_outside.append(rooms_outside[20:24])
    rooms2d_outside.append(rooms_outside[24:28])
    rooms2d_outside.append(rooms_outside[28:32])
    rooms2d_outside.append(rooms_outside[32:36])
    rooms2d_outside.append(rooms_outside[36:40])
    rooms2d_outside.append(rooms_outside[40:44])
    rooms2d_outside.append(rooms_outside[44:48])
    rooms2d_outside.append(rooms_outside[48:])


    for i in range(len(rooms2d)):
    
        for x in range(len(rooms2d[i])):
            if i == 0:
                if x == 0:
                    connectRooms(rooms2d[i][x], rooms2d[i][x+1], 'right')
                    connectRooms(rooms2d[i][x], rooms2d[i+1][x], 'down')
                elif x == 3:
                    connectRooms(rooms2d[i][x], rooms2d[i][x-1], 'left')
                    connectRooms(rooms2d[i][x], rooms2d[i+1][x], 'down')
                else:
                    connectRooms(rooms2d[i][x], rooms2d[i][x+1], 'right')
                    connectRooms(rooms2d[i][x], rooms2d[i][x-1], 'left')
                    connectRooms(rooms2d[i][x], rooms2d[i+1][x], 'down')
                    
            elif i == 12:
                if x == 0:
                    connectRooms(rooms2d[i][x], rooms2d[i][x+1], 'right')
                    connectRooms(rooms2d[i][x], rooms2d[i-1][x], 'up')
                elif x == 3:
                    connectRooms(rooms2d[i][x], rooms2d[i][x-1], 'left')
                    connectRooms(rooms2d[i][x], rooms2d[i-1][x], 'up')
                else:
                    connectRooms(rooms2d[i][x], rooms2d[i][x+1], 'right')
                    connectRooms(rooms2d[i][x], rooms2d[i][x-1], 'left')
                    connectRooms(rooms2d[i][x], rooms2d[i-1][x], 'up')
            
            else:
                if x == 0:
                    connectRooms(rooms2d[i][x], rooms2d[i][x+1], 'right')
                    connectRooms(rooms2d[i][x], rooms2d[i-1][x], 'up')
                    connectRooms(rooms2d[i][x], rooms2d[i+1][x], 'down')
                elif x == 3:
                    connectRooms(rooms2d[i][x], rooms2d[i][x-1], 'left')
                    connectRooms(rooms2d[i][x], rooms2d[i-1][x], 'up')
                    connectRooms(rooms2d[i][x], rooms2d[i+1][x], 'down')
                else:
                    connectRooms(rooms2d[i][x], rooms2d[i][x+1], 'right')
                    connectRooms(rooms2d[i][x], rooms2d[i][x-1], 'left')
                    connectRooms(rooms2d[i][x], rooms2d[i-1][x], 'up')
                    connectRooms(rooms2d[i][x], rooms2d[i+1][x], 'down')

    for i in range(len(rooms2d_outside)):
    
        for x in range(len(rooms2d_outside[i])):
            if i == 0:
                if x == 0:
                    connectRooms(rooms2d_outside[i][x], rooms2d_outside[i][x+1], 'right')
                    connectRooms(rooms2d_outside[i][x], rooms2d_outside[i+1][x], 'down')
                elif x == 3:
                    connectRooms(rooms2d_outside[i][x], rooms2d_outside[i][x-1], 'left')
                    connectRooms(rooms2d_outside[i][x], rooms2d_outside[i+1][x], 'down')
                else:
                    connectRooms(rooms2d_outside[i][x], rooms2d_outside[i][x+1], 'right')
                    connectRooms(rooms2d_outside[i][x], rooms2d_outside[i][x-1], 'left')
                    connectRooms(rooms2d_outside[i][x], rooms2d_outside[i+1][x], 'down')
                    
            elif i == 12:
                if x == 0:
                    connectRooms(rooms2d_outside[i][x], rooms2d_outside[i][x+1], 'right')
                    connectRooms(rooms2d_outside[i][x], rooms2d_outside[i-1][x], 'up')
                elif x == 3:
                    connectRooms(rooms2d_outside[i][x], rooms2d_outside[i][x-1], 'left')
                    connectRooms(rooms2d_outside[i][x], rooms2d_outside[i-1][x], 'up')
                else:
                    connectRooms(rooms2d_outside[i][x], rooms2d_outside[i][x+1], 'right')
                    connectRooms(rooms2d_outside[i][x], rooms2d_outside[i][x-1], 'left')
                    connectRooms(rooms2d_outside[i][x], rooms2d_outside[i-1][x], 'up')
            
            else:
                if x == 0:
                    connectRooms(rooms2d_outside[i][x], rooms2d_outside[i][x+1], 'right')
                    connectRooms(rooms2d_outside[i][x], rooms2d_outside[i-1][x], 'up')
                    connectRooms(rooms2d_outside[i][x], rooms2d_outside[i+1][x], 'down')
                elif x == 3:
                    connectRooms(rooms2d_outside[i][x], rooms2d_outside[i][x-1], 'left')
                    connectRooms(rooms2d_outside[i][x], rooms2d_outside[i-1][x], 'up')
                    connectRooms(rooms2d_outside[i][x], rooms2d_outside[i+1][x], 'down')
                else:
                    connectRooms(rooms2d_outside[i][x], rooms2d_outside[i][x+1], 'right')
                    connectRooms(rooms2d_outside[i][x], rooms2d_outside[i][x-1], 'left')
                    connectRooms(rooms2d_outside[i][x], rooms2d_outside[i-1][x], 'up')
                    connectRooms(rooms2d_outside[i][x], rooms2d_outside[i+1][x], 'down')

class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200428_2043'),
    ]

    operations = [
        migrations.RunPython(seed_everything),
    ]
