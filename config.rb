# require 'bootstrap-sass'
require 'compass/import-once/activate'
require 'autoprefixer-rails'
require 'growl'
# Require any additional compass plugins here.


# Set this to the root of your project when deployed:
http_path = "/"
css_dir = "application/static/styles/"
sass_dir = "sass"
images_dir = "application/static/images/"
http_images_path = "/static/images"
javascripts_dir = "application/static/js/"
fonts_dir = "application/static/fonts"
http_fonts_path = "/static/fonts"

# You can select your preferred output style here (can be overridden via the command line):
# output_style = :expanded or :nested or :compact or :compressed

# To enable relative paths to assets via compass helper functions. Uncomment:
relative_assets = true

# my_env = environment

# output_style =  (my_env == :production) ? :compressed : :expanded

project_type = :stand_alone
additional_import_paths = ["application/static/components/bootstrap-sass/assets/stylesheets/","application/static/components/bootstrap-sass/assets/stylesheets/bootstrap/"]
# additional_import_paths = ["application/static/components/bootstrap-sass/assets/stylesheets/bootstrap/"]

# add_import_path "components/bootstrap-sass/assets/"
# add_import_path "components/bootstrap-sass/assets/stylesheets/"
# add_import_path "components/bootstrap-sass/assets/stylesheets/bootstrap/"
# add_import_path "components/bootstrap-sass/assets/stylesheets/bootstrap/mixins"

# To disable debugging comments that display the original location of your selectors. Uncomment:
# line_comments = false


# If you prefer the indented syntax, you might want to regenerate this
# project again passing --syntax sass, or you can uncomment this:
# preferred_syntax = :sass
# and then run:
# sass-convert -R --from scss --to sass sass scss && rm -rf sass && mv scss sass
# print "we're in front of checking the environment\n Environment is: "

# on_stylesheet_saved do |file|
#     if my_env == :production
#       css = File.read(file)
#       map = file + '.map'
#
#       if File.exists? map
#         result = AutoprefixerRails.process(css,
#           from: file,
#           to:   file,
#           map:  { prev: File.read(map), inline: false })
#         File.open(file, 'w') { |io| io << result.css }
#         File.open(map,  'w') { |io| io << result.map }
#       else
#         File.open(file, 'w') { |io| io << AutoprefixerRails.process(css) }
#       end
#     end
# end


if environment == :development
    line_comments = true
    output_style = :nested
    sass_options = {:debug_info => true}
end

if environment == :production
    line_comments = false
    output_style = :compressed
    sass_options = {:debug_info => false}
    sourcemap = true

    on_stylesheet_saved do |file|
          css = File.read(file)
          map = file + '.map'

          if File.exists? map
            result = AutoprefixerRails.process(css,
              from: file,
              to:   file,
              map:  { prev: File.read(map), inline: false })
            File.open(file, 'w') { |io| io << result.css }
            File.open(map,  'w') { |io| io << result.map }
          else
            File.open(file, 'w') { |io| io << AutoprefixerRails.process(css) }
          end
    end

#     require 'fileutils'
#         on_stylesheet_saved do |file|
#             if File.exists?(file)
#             filename = File.basename(file, File.extname(file))
#             File.rename(file, "css" + "/" + filename + ".min" + File.extname(file))
#         end
#     end
end





Growl.notify {
    self.message = "Finished"
    sticky!
}
