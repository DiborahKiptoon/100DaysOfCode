#Variables 
#tickets
#systems
#updates

tickets = ["Ticket1", "Ticket2", "Ticket3"]
systems = ["SystemA", "SystemB", "SystemC"]
software_updates = ["Update1", "Update2", "Update3"]

# for block
#tickets
for ticket in tickets:
    print(f"Handling ticket: {ticket}")
    for close_attempt in range(3):
        print(f"Attempt {close_attempt + 1} to close {ticket}")
        
        if close_attempt < 2:
            print(f"Failed to close {ticket}, retrying...")
        else:
            print(f"Successfully closed {ticket}")
            break  
#Troubleshooting
for system in systems:
    print(f"Troubleshooting system: {system}")
    
    for troubleshooting_step in range(5):
        print(f"Step {troubleshooting_step + 1}: Attempting to resolve issues for {system}")
        
        if troubleshooting_step >= 3:
            print(f"Issue resolved for {system}")
            break

#Software updates
for update in software_updates:
    print(f"Updating software: {update}")
    
    for update_step in range(4):
        print(f"Step {update_step + 1}: Applying update {update} to the software")
        
        if update_step >= 2:
            print(f"Update {update} applied successfully")
            break
