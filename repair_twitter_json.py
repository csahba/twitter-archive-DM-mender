# 
import json
from datetime import datetime
def main():
    #  set files
    dmfiles = ["direct-messages.js", "direct-message-headers.js", "direct-messages-group.js", "direct-message-group-headers.js"]

    #  loop over files
    for dmfile in dmfiles:
        try:
            repairfile(dmfile)
        except:
            print('error with ' + dmfile)
        
def repairfile(dmfile):
    #  open file
    with open(dmfile, "r", encoding='utf8') as file:
        data = file.read()

    #  slice out variable declaration turn into valid json
    leadingstr= data[:data.find('[')]

    data = data[data.find('['):]

    #  load json into object
    dms = json.loads(data)

    #  turn into dict of conversation ids containing list of message dicts
    conversations = {}
    for x in dms:
        id = x['dmConversation']['conversationId']
        #print(id)
        if id not in conversations.keys():
            conversations[id] =  x['dmConversation']['messages']
        else:
            #conversations[id] = conversations[id] + x['dmConversation']['messages']
            #print(datetime.fromisoformat(conversations[id][0]['messageCreate']['createdAt'][:-1]))
            #print(datetime.fromisoformat(x['dmConversation']['messages'][0]['messageCreate']['createdAt'][:-1]))
            
            if (datetime.fromisoformat(conversations[id][0]['messageCreate']['createdAt'][:-1]) > datetime.fromisoformat(x['dmConversation']['messages'][0]['messageCreate']['createdAt'][:-1])):
                conversations[id] = conversations[id] + x['dmConversation']['messages']
            else:
                conversations[id] = x['dmConversation']['messages'] + conversations[id]

    #  recompile to a single list of dicts
    newconversations = []
    for id in conversations.keys():
        #print(conversations[id])
        newconversations.append( {"dmConversation" : {"conversationId" : id, "messages" : conversations[id]}} )

    #  write to new file
    outputfile = open(dmfile, "w", encoding='utf8')
    outputfile.write(leadingstr)
    json.dump(newconversations, outputfile, indent = 2, ensure_ascii=False)
    outputfile.close()

if __name__ == '__main__':
    main()