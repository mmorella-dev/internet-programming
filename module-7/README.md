# module-7 - Python CGI App

## Disclaimer

Apache configurations are not portable, so executing this project locally (especially on a different operating system), may be a challenge.

Per the no warranty clause of the MIT license in the root directory, these instructions are not guaranteed to work.

## Usage

1. Install the Apache HTTP server.
   * `brew install httpd`
   * Alternatively, download and install the XAMPP stack.
1. Move the files in ./module-7/htdocs into your DocumentRoot.
     * On macOS, I created a symlink:
       ```sh
       rm /usr/local/var/www # homebrew puts httpd docroot here
       ln -s $PWD/module-7/htdocs /usr/local/var/www
       ```
1. Enable the CGI module in httpd.conf:

     * ```xml
       <IfModule !mpm_prefork_module>
         # -- uncomment this line --
         LoadModule cgid_module lib/httpd/modules/mod_cgid.so
       </IfModule>
       <IfModule mpm_prefork_module>
         # -- also uncomment this line --
         LoadModule cgi_module lib/httpd/modules/mod_cgi.so
       </IfModule>
       ```
1. Configure httpd.conf to allow executing CGI files:
     * ```xml
       <Directory "/usr/local/var/www/cgi-bin">
         AllowOverride None
         Options ExecCGI
         Order allow,deny
         Allow from all
       </Directory>
       ```

1. Start the Httpd server, and navigate to the page in your web browser.