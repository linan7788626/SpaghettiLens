
LMT.utils.logger = function () {
  this.log = document.getElementById("logcont");
  
  this.write = function(txt) {
    this.log.innerHTML = txt;
  };
  
  this.append = function(txt) {
    this.log.innerHTML += ('<br/>' + txt); 
  };
  
  this.clear = function() {
    this.log.innerHTML = ""; 
  };
}



/**************
 * Math helpers 
 */

LMT.utils.toPolarAng = function(xdiff, ydiff) {
  var direction = (Math.atan2(ydiff, xdiff));
  return (direction);
}

LMT.utils.toPolarR = function(xdiff, ydiff) {
  var distance = Math.sqrt(xdiff * xdiff + ydiff * ydiff);
  return (distance);
}

LMT.utils.toRectX = function(direction, distance) {
  var x = distance * Math.cos(direction);
  return (x);
}

LMT.utils.toRectY = function(direction, distance) {
  var y = distance * Math.sin(direction);
  return (y);
}

/**
 * calculates the distance squarred between to point like objects (have .x and .y attribute) 
 */
LMT.utils.dist2 = function(pnt1, pnt2) {
  var dx = pnt1.x-pnt2.x;
  var dy = pnt1.y-pnt2.y;
  return (dx*dx+dy*dy);
}



/**
 * addons to jquery
 */


/**
 * svg manipulation addon
 * (since addclass doesnt work for svg dom elements, but .attr does)
 * classList does not exist in IE, see here for comatibility lib
 * https://developer.mozilla.org/en-US/docs/DOM/element.classList
 * 
 */
$.fn.addClassSVG = function(classname) {
	return this.each(function() {
		this.classList.add(classname)});
}

LMT.utils.removeClassSVG = function($sel, classname) {
	return this.each(function() {
		this.classList.remove(classname)});
}

LMT.utils.toggleClassSVG = function($sel, classname) {
	return this.each(function() {
		this.classList.toggle(classname)});
}

