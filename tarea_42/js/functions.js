
window.artyom = new Artyom();

var video = document.getElementById("myvideo");
var span = document.getElementById('output');
var span2 = document.getElementById('output2');
var helloText = "Welcome. My name is Lisa. Let's practice English. Speak to me and I'll write what you say"
var text2 = "It was fun to speak with you. Let continue another day. See you, have a nice day"
var textListen = ""
var slider = document.getElementById("myRange");
var sliderValue = 50

function UpdateSlider(){
  var output = document.getElementById("outputVar");

  console.log('value change');
  console.log(slider.value);
  output.innerHTML = slider.value/50;
  sliderValue = slider.value;
}

artyom.addCommands([
    {
        description:"Artyom can talk too, lets say something if we say hello",
        indexes:["hello", "hey", "Bonjour"],
        action:function(i){
            console.log("Something matches")
            if(i == 0){
                saySomething(helloText);
            }
        }
    },
    {
        description:"Artyom can talk too, lets say somethin if we say hello",
        indexes:["bye", "goodbye", "See you"],
        action:function(i){
            console.log("Something matches")
            video.pause()
            if(i == 0){
                alert("Now all is over");
                saySomething(text2);
            }
        }
    },
    {
        indexes:["goodbye"],
        action:function(){
            video.pause()
            alert("Now all is over");
        }
    },
    {
        indexes:["stop"],
        action:function(i){
            video.pause()
        }
    },
    {
        indexes:["play"],
        action:function(i){
            console.log("match: adelante")
            console.log(i)
            video.play()
        }
    },
]);
artyom.redirectRecognizedTextOutput(function(text, isFinal){

    if(isFinal){
        span.innerHTML = text;
        span2.innerHTML = text;
        saySomething(text)
        textListen = text;

    }else {
        span.innerHTML = text;
    }
});
function startArtyom(){
    artyom.initialize({
//            lang:"fr-FR",
//            lang:"es-ES",
        lang:"en-US", // A lot of languages are supported. Read the docs !
        continuous:false, // recognize 1 command and stop listening !
        debug:true, // Show everything in the console
        listen:true, // Start recognizing
        speed: Math.floor(sliderValue/50)
    });
    console.log('start')
    console.log(slider.value)
//    saySomething(helloText)

}
function stopArtyom(){
    span2.innerHTML = text2;
    saySomething(text2);
    artyom.fatality();
    video.pause()
}
function repeatArtyom(){
    saySomething(textListen);
}
function saySomething(txt){
    artyom.say(txt)
    }