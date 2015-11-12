var stopped = false;
var size = "30x30"
var lifecell = jsboard.piece({text:"1", fontSize: "14px", textIndent:"-9999px", background: "black"});
var b = jsboard.board({ attach: "game", size: size });

b.style({borderSpacing: "1px", margin: "0 auto", marginTop: "6px",});
b.cell("each").style({width: "17px", height: "17px", background: "lightblue"});

b.cell("each").on("click", function() {
    if (b.cell(this).get()===null) {
        b.cell(this).place(lifecell.clone());
    } else {
	b.cell(this).rid()
    }
});

function convertNullsToZero(grid) {
    for(var col = 0; col < grid.length; col++) {
        for(var row = 0; row < grid[col].length; row++) {
            if(grid[col][row]===null){
                grid[col][row]=0;
	    }
	}
    };
    return grid;
};

function arrayToJson(current_json) {
    return JSON.stringify(current_json);
};

function updateGrid(next_grid) {
    for(var col = 0; col < next_grid.length; col++) {
        for(var row = 0; row < next_grid[col].length; row++) {
            if(next_grid[col][row] == 1) {
                b.cell([col,row]).place(lifecell.clone());
            }
            else {
                b.cell([col,row]).rid();
            }
        };
    };
};

function rawCellValues(grid) {
    return arrayToJson(grid).replace(/\D/g,'');
};

function nextGrid(current_grid) {
    $.post("/game", arrayToJson(current_grid), function(data) {
	updateGrid(data);
	if(rawCellValues(current_grid) != rawCellValues(data) && !stopped) {
            setTimeout(function() { nextGrid(convertNullsToZero(b.matrix())) }, 150);
	} else {
	    stopped = true;
	}
    });
};

function startSim() {
    nextGrid(convertNullsToZero(b.matrix()));
};

function stopSim() {
    stopped = true;
};

function resetSim() {
    stopped = true;
    b.cell("each").rid();
}

document.getElementById("start").addEventListener("click", function() { stopped = false; startSim(); });
document.getElementById("stop").addEventListener("click", function() { stopSim(); });
document.getElementById("reset").addEventListener("click", function() { resetSim(); });
