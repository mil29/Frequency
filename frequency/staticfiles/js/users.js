$(document).ready(function() {



var frequencyslider = document.getElementById("frequencyRange");
var frequencyoutput = document.getElementById("frequencydemo");
var boostslider = document.getElementById("boostRange");
var boostoutput = document.getElementById("boostdemo");
var cutslider = document.getElementById("cutRange");
var cutoutput = document.getElementById("cutdemo");
var khzorhz = document.getElementById("khzrange");
var frequencyInput = document.getElementById("frequencyInput");



frequencyoutput.innerHTML = frequencyslider.value + ' Hz';
boostoutput.innerHTML = boostslider.value;
cutoutput.innerHTML = cutslider.value;


frequencyslider.oninput = function() { // when frequency slider is moved css removes hidden state and adjusts frequencyoutput html with either Hz or kHz

    if (this.value >= 1000){
        frequencyoutput.innerHTML = this.value +' kHz';
    } else {
        frequencyoutput.innerHTML = this.value + ' Hz';
    }
}

frequencyslider.onchange = function(){  // the frequency input adjusts to frequency slider movement
    frequencyInput.value = frequencyslider.value;
};
frequencyInput.onkeyup = function(){  // the range slider adjusts to the frequency input 
      frequencyslider.value = frequencyInput.value;  
    if (frequencyInput.value >= 1000){
        frequencyoutput.innerHTML = frequencyInput.value + ' kHz';
    } else {
        frequencyoutput.innerHTML = frequencyInput.value + ' Hz';
    }
    };  

boostslider.oninput = function() {  // shows the boost value 
    $(boostoutput).removeClass("hidden");
    boostoutput.innerHTML = this.value;
}
cutslider.oninput = function() {   // shows the cut value
    $(cutoutput).removeClass("hidden");
    cutoutput.innerHTML = this.value;
}


});
