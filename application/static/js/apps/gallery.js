define(["jquery","jquery.hammer","jquery-ui"],function($){

    var options = {
        main_gallery_image:         "#gallery-main",
        fullsize_path:              "static/images/PreviewImages/fullsize",
        path_location:              location.origin,
        active_class:               "gallery-thumbnail-active",
        select_class:               ".gallery-thumbnail",
        gallery_thumbnail_link:     ".gallery-thumbnail-link",
    };

    options["my_selector"] = "a"+options.gallery_thumbnail_link;

    var main_image = $(options.main_gallery_image);
    var large_image_url = options.fullsize_path;
    var image_count = $(options.my_selector).size()-1
    
    /** take image name and index and show it **/
    function ShowBigImage( image_name, image_index ) {
        src_url = large_image_url + "/" + image_name;
        main_image.attr("src",src_url);
        main_image.attr("data-index",image_index);
        main_image.show("fade", 500);
    }

    /** Determine what direction and which image was swiped **/
    function SwipeImage(swipe_direction,image_index){
      if( swipe_direction == 2 || swipe_direction == 1 ){
        image_index = image_index + 1;
      }

      if( swipe_direction == 4 ){
        image_index = image_index - 1;
      }

      if( image_index > image_count ){
        image_index = 0;
      }
      
      if( image_index < 0 ) {
          image_index = image_count;
      }

      var thumbnail_image = $($(options.select_class).get(image_index));
      var selected_image = thumbnail_image.attr("data-title");
      $("."+options.active_class).removeClass(options.active_class);
      thumbnail_image.addClass(options.active_class);
        
      ShowBigImage(selected_image, image_index);

      }


    return {
        preview: function(){


            $(options.my_selector).on("click", function(event){
                $("."+options.active_class).removeClass(options.active_class);
                $(event.target).addClass(options.active_class);
                var image_title = $(event.target).attr("data-title");
                image_index = $(options.my_selector).index(this);
                ShowBigImage(image_title, image_index);
                event.preventDefault();
              });

            $(options.main_gallery_image).hammer().bind("swipe tap", function(e){
              var image_index = 0;
              var swipe_direction = e.gesture.direction;
              image_index = parseInt($(e.target).attr("data-index"));
              
              SwipeImage(swipe_direction,image_index);
            });

    }
    }
});
