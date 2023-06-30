function loadCustomNavbar(){
    var customNavBar =  `
                       <!---MENU-->
 <nav class="navbar navbar-expand-lg navbar-dark bg-dark #2c313c">
     <div class="container-fluid">
     <a class="navbar-brand" href="index.html">
         <img src="img/logo-footer.png" alt="Logo" width="120px">
     </a>
     <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent"
      aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
         <span class="navbar-toggler-icon"></span>
     </button>
     <div class="collapse navbar-collapse" id="navbarSupportedContent">
         <ul class="navbar-nav me-auto mb-2 mb-lg-0">
         <li class="nav-item">
             <a class="nav-link active" aria-current="page" href="#quienesSomos">
                 Quienes Somos</a>
         </li>
         <li class="nav-item">
             <a class="nav-link" href="formulario.html">Agenda Hora</a>
         </li>
         <li class="nav-item">
             <a class="nav-link active" aria-current="page" href="#contacto">
                 Contacto</a>
         </li>
         <li class="nav-item dropdown">
             <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
             Nuestros Cortes 
             </a>
             <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
             <li><a class="dropdown-item" href="carruselmujer.html">Cortes Mujer</a></li>
             <li><a class="dropdown-item" href="carrusel.html">Cortes Hombres</a></li>
             <li><a class="dropdown-item" href="carruselninos.html">Cortes Niños</a></li>
             </ul>
         </li>
         </ul>
         
     </div>
     </div>
 </nav>
                       
                       
  `;

    var customNabBarHTML = document.getElementById("custom-navbar");
    customNabBarHTML.innerHTML = customNavBar;
}

loadCustomNavbar();