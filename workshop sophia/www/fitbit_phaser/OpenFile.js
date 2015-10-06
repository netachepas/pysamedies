Fitbit.OpenFile = function (game) {

	this.music = null;
	this.playButton = null;
	var lines = [];
	var muziekBezig;

};

Fitbit.OpenFile.prototype = {

	create: function () {
        //variables globales: initialisation
        lines = [];
        muziekBezig = 1;
		//	We've already preloaded our assets, so let's kick right into the Main Menu itself.
		//	Here all we're doing is playing some music and adding a picture and button
		//	Naturally I expect you to do something significantly better :)
		console.log("Nu zijn we in openfile")



		this.playButton = this.add.button(200, 300, 'button-start', this.zoekFile, this, 1, 0, 2);
		//laatste drie parameters zijn de frames: button over, button out..

	},

	update: function () {

		//	Do some nice funky main menu effect here

	},

	zoekFile: function (pointer) {
	//zoekFile: function () {

		//	Ok, the Play Button has been clicked or touched, so let's stop the music (otherwise it'll carry on playing)
		//this.music.stop();
		//this.music.stop();
		//	And start the actual game
		//this.state.start('Game');

        //ceci ouvre un dialog window ou on peut browser vers le fichier
		console.log("Maintenant nous ouvrons le fichier")
		var input = document.createElement("INPUT");
        input.setAttribute("type", "file");
        input.setAttribute("id", "fileinput");
        document.body.appendChild(input);
        input.addEventListener("change", this.fileChosen.bind(this));
        input.click();
        document.body.removeChild(input);
    },


    fileChosen: function(e) {
        var fr = new FileReader();
        fr.onload = receivedText.bind(this);
        fr.readAsText(e.currentTarget.files[0]);

        function receivedText(e) {

            //lines = e.target.result;
            //console.log(lines);
            //var tempObj = JSON.parse(lines);

            allText = e.target.result;
            var allTextLines = allText.split(/\r\n|\n/);
            var a = allTextLines.indexOf("Activit" + "\u00e9" + "s");
            var b = allTextLines.indexOf("Sommeil");
            //console.log(a);
            //console.log(b);

            //var headers = allTextLines[0].split(',');       //split op komma
            var headers = allTextLines[a+1].split(',');       //split op komma
            //console.log(headers.length);
            //console.log(allTextLines.length);

            //var lines = [];

            //for (var i=1; i<allTextLines.length; i++) {

            for (var i=a+2; i<b-1; i++) {
            // for (var i=226; i<246; i++) {
                var data = allTextLines[i].split(',');
                //console.log(data);
                //if (data.length == headers.length) {

                    //var tarr = [];
                    //for (var j=0; j<headers.length; j++) {
                    //    //tarr.push(headers[j]+":"+data[j]);  //voor dictionary
                    //    tarr.push(data[j]);                     //voor 2d array

                    //}

                    //lines.push(tarr);


                        //console.log(data[2]);

                        var zz = data[2];
                        var res1 = zz.replace(/\s+/g,""); //verwijder alle whitespace met regular expression
                        var res2 = res1.replace("\"", "");  //verwijder de " uit de cvs velden
                                                            //die niets te maken hebben met een string variabele
                                                            //maar een gewone character zijn
                        var res = res2.replace("\"", "")     //doe het nog eens voor de " op het einde van het veld
                        //console.log(res);
                        var s = Number(res);
                        //console.log(s);

                        //console.log(res);
                        //var z = parseInt(res);
                        //if (z.substring)
                        //{
                        // do string thing
                        //console.log("het is een string");
                        //} else{
                        // do other thing
                        //console.log("het is geen string");

                        //}
                        //if (s.toFixed) {
                            // do number thing
                        //     console.log("het is een number");
                        //  } else {
                            // do other thing
                        //     console.log("het is geen number");
                        //}
                     if (s > 0){
                        lines.push(s);

                     }

                //}
            }
            //console.log(lines);
            //var ss = "mijn string";
            //var ress = ss.replace(" ", "");
            //console.log(ress);

            this.gaNaarStart()
            //this.playButton = this.add.button(200, 300, 'button-start', this.gaNaarStart, this, 1, 0, 2);
		//laatste drie parameters zijn de frames: button over, button out..


        }
    },










	//gaNaarStart: function (pointer) {     //als via button verloopt
	gaNaarStart: function () {

		//	Ok, the Play Button has been clicked or touched, so let's stop the music (otherwise it'll carry on playing)
		//this.music.stop();
		console.log("ga naar main button")
		//this.music.stop();
		//	And start the actual game
		this.state.start('Game');

	}


};
