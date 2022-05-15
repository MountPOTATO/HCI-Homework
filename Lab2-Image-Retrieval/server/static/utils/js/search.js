var favoriteSet=new Set();



function showImg(input) {
  var file = input.files[0];
  var reader = new FileReader()
  reader.readAsDataURL(file)

  reader.onload = function (reader) {
      document.getElementById("previmg").src=reader.target.result;
      document.getElementById("previmg").style.display="block";
  }
}

function changeFavIcon(x,num) {

  x.classList.toggle("fa-heartbeat");

  // 如果有收藏
  if(x.classList.contains("fa-heartbeat")){
    var dis=document.getElementById("img"+num).src;
    console.log(dis);
    favoriteSet.add(dis);
  }
  else{
    var dis=document.getElementById("img"+num).src;
    console.log(dis);
    favoriteSet.delete(dis);
  }

  console.log(favoriteSet)

  
}

function dropFunction() {
  var x = document.getElementById("myDIV");
  if (x.className.indexOf("w3-show") == -1) {
    x.className += " w3-show";
  } else {
    x.className = x.className.replace(" w3-show", "");
  }
}



function fun(){

                
	$("form").submit(function(evt){	 
		
        document.getElementById("gif").style.display="block";
                        
        evt.preventDefault();
            

        var formData = new FormData($(this)[0]);
            
        $.ajax({
            url: 'imgUpload',
            type: 'POST',
            data: formData,
            //async: false,
            cache: false,
            contentType: false,
            enctype: 'multipart/form-data',
            processData: false,
            
            success: function (response) {

            console.log(response);

            for(let i=0;i<6;i++){
                if(favoriteSet.has(document.getElementById("img"+i).src)){
                    document.getElementById("icon"+i).classList.remove("fa-heartbeat");
                }
            }

            var tagSets=new Set();

            document.getElementById("gif").style.display="none";
            document.getElementById("search-results").style.display="block";         
            document.getElementById("img0").src = response.image0[0];
            document.getElementById("tag0").innerHTML = response.image0[1];
            document.getElementById("img1").src = response.image1[0];
            document.getElementById("tag1").innerHTML = response.image1[1];
            document.getElementById("img2").src = response.image2[0];
            document.getElementById("tag2").innerHTML = response.image2[1];
            document.getElementById("img3").src = response.image3[0];
            document.getElementById("tag3").innerHTML = response.image3[1];
            document.getElementById("img4").src = response.image4[0];
            document.getElementById("tag4").innerHTML = response.image4[1];
            document.getElementById("img5").src = response.image5[0]
            document.getElementById("tag5").innerHTML = response.image5[1];


            if(favoriteSet.size!=0){
                for(let i=0;i<6;i++){
                    if(favoriteSet.has(document.getElementById("img"+i).src)){
                        document.getElementById("icon"+i).classList.toggle("fa-heartbeat");
                    }
                }
            }

            for(let i=0;i<6;i++){
                tagSets.add(document.getElementById("tag"+i).innerHTML);
            }



            var tagl=[...tagSets]

            var it=tagSets.values();

            var tag_name_list=["fig0","fig1","fig2","fig3","fig4","fig5"];

            document.getElementById("figAll").textContent="all";
            document.getElementById("figAll").style.display="block";

            for(var i=0;i<tagl.length;i++){
                document.getElementById(tag_name_list[i]).textContent=tagl[i]
                document.getElementById(tag_name_list[i]).style.display="block";
            }

            for(var i=tagl.length;i<6;i++){
                document.getElementById(tag_name_list[i]).style.display="none";
            }

            
                    
    
        }
    });

    return false;
})};

       
function addFavPic(){

    document.getElementById('favor-modal').style.display='block'

    console.log("yes")
    var ilist=[...favoriteSet]

    var element = document.getElementById("imglist");
    element.innerHTML=""

    for(let i=0;i<ilist.length;i++){
        var tag = document.createElement("img");
        tag.src=ilist[i];
        tag.style="width:100px;height:100px;padding:2%";
        element.appendChild(tag)
        
    }
}


function returnHome(){
    document.getElementById("previmg").style.display="none";
    document.getElementById("search-results").style.display="none";
}
