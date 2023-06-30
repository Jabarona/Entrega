function loadCustomFooter(){
    var customFooter =  `
                       
 
    <!--PIE DE PAGINA-->
    <section class="" id="contacto">
    <footer class="pie-pagina">
        <div class="grupo-1">
            <div class="box">
                <figure>
                    <a href="#">
                        <img src=" img/logo-footer.png" alt="logo barberia">
                    </a>
                </figure>
            </div>
            <div class="box">
                <h1>CONTACTANOS</h1>
                <p></p>
                <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d11196.49261435402!2d-70.66355930180579!3d-33.45615347432367!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x9662c50ece08b569%3A0x2fb0a2e7986d894c!2sParque%20Almagro!5e0!3m2!1ses-419!2scl!4v1680885323173!5m2!1ses-419!2scl" 
                width="100%" height="250" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
                
                
            </div>
            <div class="box">
                <h2>SIGUENOS EN NUESTRAS REDES</h2>
                <div class="red-social">
                    <a href="https://www.instagram.com/scrapy.cc/" target="_blank"
                    class=" fa fa-instagram"></a>
                    <a href="https://web.facebook.com/profile.php?id=100091445451404" target="_blank"
                    class=" fa fa-facebook"></a>
                    <a href="https://wa.me/56931085509?text=Hola quiero agendar un turno." target="_blank" 
                    class=" fa fa-whatsapp"></a>
                </div>
            </div>
        </div>
        <div class="grupo-2">
            <small>&copy;2023 <b>APRENDIENO HTML</b> </small>
        </div>
    </footer>
    </section>
 

   
                       
  `;

    var customFooterHTML = document.getElementById("custom-footer");
    customFooterHTML.innerHTML = customFooter;
}

loadCustomFooter();