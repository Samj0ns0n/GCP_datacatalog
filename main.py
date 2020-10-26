import Read_write as rw
from pattern_matching import pattern_match
from action import actions



if __name__ == "__main__":
    
    # Vous serez devant la page du bucket que vous voulez
    # En face de vous il y aura le nom du bucket
    
    #bucket_name = input("Selectionner le nom du bucket : ")
    #path_to_csv = rw.selection(bucket_name)
    #blob_metadata(bucket_name, path_to_csv)
    actions("test-datapod","Test_header_virgule.csv")


  
   