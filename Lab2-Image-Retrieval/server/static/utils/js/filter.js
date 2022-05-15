function filter(num){

    for(let i=0;i<6;i++){
        document.getElementById("img"+i).style.opacity="1";
        document.getElementById("t"+i).style.display="block";
        document.getElementById("icon"+i).style.display="block";
    }


    if(num!=-1){
        var tagContent=document.getElementById("tag"+num).innerHTML;
        for(let i=0;i<6;i++){
            if(document.getElementById("tag"+i).innerHTML!=tagContent){
                document.getElementById("img"+i).style.opacity="0.1";
                document.getElementById("t"+i).style.display="none";
                document.getElementById("icon"+i).style.display="none"; 
            }
        }
    }
}