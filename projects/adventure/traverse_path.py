

def traverse_path(world):
    # Bring in length of rooms
    num_rooms = len(world.rooms)
    # print(num_rooms)
    # Create return path for later
    return_path = []
    # Create visited set to store all visited rooms
    visited = set()

    # Initiate starting room cases (add to visited and return_path)
    current_room = world.startingRoom
    # print(current_room)
    visited.add(current_room)
    return_path.append(current_room)
    # print(len(visited))

    # Loop while we haven't found all rooms
    # Two loops. Outer loop for adding the initial 4 rooms, and the inner loop for traversing the paths of those 4 rooms
    while(len(visited) < num_rooms):

        # Check all directions to see if they exist in your current room (if statements)
        connected_rooms = []
        if current_room.n_to:
            connected_rooms.append(current_room.n_to)
        if current_room.s_to:
            connected_rooms.append(current_room.s_to)
        if current_room.e_to:
            connected_rooms.append(current_room.e_to)
        if current_room.w_to:
            connected_rooms.append(current_room.w_to)
        # Set this up for next loop. If all rooms are explored, then that means this is last room
        unexplored_connected_rooms = False
        # print(f'Connected Rooms:{connected_rooms}')

        # Loop through all connections and if there is a direction and it isn't in visited, then tag it as unexplored. Otherwise, remove it
        for c in connected_rooms:
            if c not in visited:
                unexplored_connected_rooms = True
            else:
                connected_rooms.remove(c)

        # Check all unexplored rooms in the connected_rooms list, add them to visited and return path, then set them to false.
        while unexplored_connected_rooms == True:
            current_room = connected_rooms[0]
            # print(current_room)
            visited.add(current_room)
            return_path.append(current_room)
            # Loop through this room's potential directions like I did above
            connected_rooms = []
            if current_room.n_to:
                connected_rooms.append(current_room.n_to)
            if current_room.s_to:
                connected_rooms.append(current_room.s_to)
            if current_room.e_to:
                connected_rooms.append(current_room.e_to)
            if current_room.w_to:
                connected_rooms.append(current_room.w_to)

            unexplored_connected_rooms = False

            # Recheck the rooms. This should remove the room we just traversed
            for c in connected_rooms:
                if c not in visited:
                    unexplored_connected_rooms = True
                else:
                    connected_rooms.remove(c)

        # Update path with this loop's iteration of current room
        new_path = bfs(current_room, visited)
        current_room = new_path[-1]
        visited.add(current_room)
        # Append it to path up above
        # print(f'RETURN PATH:{return_path}')
        return_path += new_path

    # return path is full of objects. need to loop through and spit out directions based on return_path[i] and return_path[i+1]
    final_path = []
    for i in range(0, len(return_path)-1):
        # print(return_path[i])
        if return_path[i].n_to == return_path[i+1]:
            final_path.append("n")
        if return_path[i].s_to == return_path[i+1]:
            final_path.append("s")
        if return_path[i].e_to == return_path[i+1]:
            final_path.append("e")
        if return_path[i].w_to == return_path[i+1]:
            final_path.append("w")

    print(f'FINAL PATH:{final_path}')
    return final_path


def bfs(room, visited_rooms):
    # print(visited_rooms)
    visited = set()
    queue = [[room]]

    while queue:
        path = queue.pop()
        vertex = path[-1]

        # print(f'VERTEX ID:{vertex.id}')

        if vertex.id not in visited:
            if vertex not in visited_rooms:
                # Slice the first element of path off
                return path[1:]
            visited.add(vertex.id)

            connected_rooms = []
            # If direction exists AND the id isnt in visited, then add to the list.
            if vertex.n_to and vertex.n_to.id not in visited:
                connected_rooms.append(vertex.n_to)
            if vertex.e_to and vertex.e_to.id not in visited:
                connected_rooms.append(vertex.e_to)
            if vertex.s_to and vertex.s_to.id not in visited:
                connected_rooms.append(vertex.s_to)
            if vertex.w_to and vertex.w_to.id not in visited:
                connected_rooms.append(vertex.w_to)
            for r in connected_rooms:
                new_path = list(path)
                new_path.append(r)
                queue.insert(0, new_path)
