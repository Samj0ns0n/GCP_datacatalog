from Read_write import selection
from pattern_matching import pattern_match
from action import actions



if __name__ == "__main__":
    
    # Vous serez devant la page du bucket que vous voulez
    # En face de vous il y aura le nom du bucket
    
    # bucket_name = input("Selectionner le nom du bucket : ")
    bucket_name = 'test-datapod'
    csv_file = selection(bucket_name)
    actions(bucket_name,csv_file[0])
    # actions("test-datapod","Test_header_virgule.csv")


  
   
