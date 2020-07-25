let source = {
  'Name':"Dougey",
  'Direction':0,
  'x':1,
  'y':1
};

function move(x,y){
  
    
  
     
    let decision = confirm(`Do you want to move to these coordinates:\n ${source.x}, ${source.y}`);
    if (decision == true){
  
      let current_location = {
        'x':source.x,
        'y':source.y
        };
  
      // alert(`Your starting location is: \n ${current_location.x}, ${current_location.y}`);
  
  
        var destination = {
          'x':x,
          'y':y
        };
  
  
        // #get the length of each coordinate change
        let len_x = Math.abs(current_location.x - destination.x);
        let len_y = Math.abs(current_location.y - destination.y);
  
        let distance = 0;
  
        // # get the distance to the objective 
        if (len_x >= len_y){
          distance = len_x;
        }else{
          distance = len_y;
        }
  
        // alert(`Perfect, your destination is ${distance} yards away`);
  
  
      // # now outside the loop, create another loop for each yard you move. It should do the following: find the shortest path between two points, determine look direction. 
      while (distance > 0){
        len_x = Math.abs(current_location["x"] - destination['x']);
        len_y = Math.abs(current_location["y"] - destination['y']);
        let combined = current_location['x'] + ',' + current_location['y'];
  
        document.getElementById(combined).innerHTML = '-';
        if (len_x > len_y){
          // #moving left/West
          if (current_location['x'] > destination['x']){
            source.Direction = 6;
            current_location['x'] -= 1;
            source.x = current_location.x;
            source.y = current_location.y;
            // alert("You move 1 yard West")
          // #moving righ/East
          }else{
            source.Direction = 2;
            current_location['x'] += 1;
            source.x = current_location.x;
            source.y = current_location.y;
            // alert("You move 1 yard East");
          }
  
        } else if (len_x < len_y){
          // #moving down/South
          if (current_location['y'] > destination['y']){
            source.Direction = 4;
            current_location['y'] -= 1;
            source.x = current_location.x;
            source.y = current_location.y;
            // alert("You move 1 yard South");
          // #moving up/North
          }else{
            source.Direction = 0;
            current_location['y'] += 1;
            source.x = current_location.x;
            source.y = current_location.y;
            // alert("You move 1 yard North");
          }
  
        }else{
          // #moving up+right/North East
          if (current_location['y'] < destination['y'] && current_location['x'] < destination['x']){
            source.Direction = 1;
            current_location['x'] += 1;
            current_location['y'] += 1;
            source.x = current_location.x;
            source.y = current_location.y;
            // alert("You move 1 yard North East");
  
          // #moving down+right/South East
          }else if (current_location['y'] > destination['y'] && current_location['x'] < destination['x']){
            source.Direction = 3;
            current_location['x'] += 1;
            current_location['y'] -= 1;
            source.x = current_location.x;
            source.y = current_location.y;
            // alert("You move 1 yard South East");
  
          // #moving down+left/South West
          }else if (current_location['y'] > destination['y'] && current_location['x'] > destination['x']){
            source.Direction = 5;
            current_location['x'] -= 1;
            current_location['y'] -= 1;
            source.x = current_location.x;
            source.y = current_location.y;
            // alert("You move 1 yard South West");
  
          // #moving up+left/North West
          }else{
            source.Direction = 7;
            current_location['x'] -= 1;
            current_location['y'] += 1;
            source.x = current_location.x;
            source.y = current_location.y;
            // alert("You move 1 yard North West")
          }
          }
        combined = current_location['x'] + ',' + current_location['y'];
        document.getElementById(combined).innerHTML = source.Name;
        distance -= 1
      }
  
      // alert(`Your final coordinates are:\n  ${source.x}, ${source.y}`)
    }else{
      alert("Select another location");
    }
  }