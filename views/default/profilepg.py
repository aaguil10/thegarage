{{extend 'layout.html'}}
<!--  -->



<html lang="en">
<head>
	<style type="text/css" media="screen, print, projection">
	body,
    html {
		margin:0;
		padding:0;
	}

	#wrap {
		width:750px;
		margin:0 auto;
	}

	#main {
		float:left;
		width:80%;
		padding:5px;
        overflow:hidden;
	}
    #page-wrap { 
        width: 600px; 
        margin: 15px auto; 
        position: relative; 
    }

     #sidebar { 
        width: 200px; 
        position: fixed;
        margin-left: 920px;
        background: #D9D9F3
    }

    #footer {
		clear:both;
		padding:5px 10px;

	}

	h2 {
		margin:0 0 1em;
	}

        /*bebox are the squares that display recently added items*/
    div.bebox{
        width:200px;
        height:200px;
        border:4px solid black;
        margin-right:10px;
        margin-bottom:10px;
        padding:5px;
        float:left;
        overflow:hidden;
    }
        
        /*beboxTitle is the tile of item in bebox this class should always be inside bebox */
    div.beboxTitle{
        border:1px solid blue;
        font-size:20px
        padding:5px;
            
        }

	</style>
    {{=A('Add Item', _href=URL(r=request, f='create'), _class='btn')}}
    {{=A('Edit Profile', _href=URL(r=request, f='editprofile'), _class='btn')}}
    <!--This is the search bar... does not work yet -->
<center>
    <form id="cse-search-box" action="http://google.com/cse">
        <input type="hidden" name="cx" value="YOUR SEARCH ENGINE ID goes here" />
        <input type="hidden" name="ie" value="UTF-8" />
        <input type="text" name="q" size="15" />
        <input type="submit" name="sa" value="Search" />
    </form>
</center>
    
    


</head>
<body>

<!-- main holds the beboxes. takes 80% of page while side bar takes 20% of the page -->
	<div id="main">
		<h2>Recently Borrowed</h2>
		<div class="bebox" align="center">
            <div class="beboxTitle">
                Blue Jeans (New)
            </div>
            <img src="http://images01.olx.in/ui/6/88/96/1366443904_503408296_4-jeans-Home-Lifestyle.jpg" alt="Smiley face" max-height:100%>
        </div>

        <div class="bebox" align="center">
            <div class="beboxTitle">
                Little Brother
            </div>
            <img src="http://www.artfire.com/uploads/product/6/426/55426/2755426/2755426/large/for_sale_little_brother_by_big_brother_boys_custom_toddler_kids_shirt_24c9a2eb.jpg" alt="Smiley face" >
        </div>

        <div class="bebox" align="center">
             <div class="beboxTitle">
                Assassins Creed III(XBox 360)
            </div>
            <img src="http://st.gdefon.com/wallpapers_original/wallpapers/345928_assassins-creed_yecio_ubijca_klinki_igra_1280x1024_(www.GdeFon.ru).jpg" alt="Smiley face" >
        </div>
        
        <div class="bebox" align="center">
             <div class="beboxTitle">
                CS 101 Textbook
            </div>
            <img src="http://upload.wikimedia.org/wikipedia/en/4/41/Clrs3.jpeg" alt="Smiley face" >
        </div>

	</div>
    
<!-- code for side bar, should make a categories page and link that to the buttons. -->
	<div id="sidebar">
		<h2>Categories</h2>
		<p>Looking for something specific?</p>
		<ul>
			<li><a href="/">Books</a></li>
			<li><a href="/">Games</a></li>
			<li><a href="/">Electronics</a></li>
			<li><a href="/">Clothing</a></li>
			<li><a href="/">Food</a></li>
		</ul>
	</div>
	

</body>
</html>
