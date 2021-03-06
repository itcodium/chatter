/**
 * chatUI constructor
 * @constructor
 * @param {d3-selection} container - Container for the chat interface.
 * @return {object} chatUI object
 */
var chatUI = (function (container) {
  
  var module = {};

  module.container = container.append('div').attr('id', 'cb-container');
  module.config = null;
  module.bubbles = [];
  module.ID = 0;
  module.keys = {};
  module.types = {};
  module.inputState = false;
  module.height = 0;
  module.scroll = module.container.append('div').attr('id', 'cb-flow');
  module.flow = module.scroll.append('div').attr('class', 'cb-inner');
  module.input = module.container.append('div').attr('id', 'cb-input').style('display', 'none');
  module.input.append('div').attr('id','cb-input-container').append('input').attr('type', 'text');
  module.input.append('button').text('+');


  /**
   * updateContainer should be called when height or width changes of the container changes
   * @memberof chatUI
   */
   module.updateContainer = function(){
      module.height = module.container.node().offsetHeight;
      module.flow.style('padding-top', module.height+'px');
      module.scroll.style('height', (module.height-((module.inputState==true)?77:0))+'px');
      module.scrollTo('end');
  };

  /**
   * @memberof chatUI
   * @param {object} options - object containing configs {type:string (e.g. 'text' or 'select'), class:string ('human' || 'bot'), value:depends on type}
   * @param {function} callback - function to be called after everything is done
   * @return {integer} id - id of the bubble 
   */
  module.addBubble = function (options, callback) {
    callback = callback || function () { };

    if (!(options.type in module.types)) {
      throw 'Unknown bubble type';
    } else {

      module.ID++;
      var id = module.ID;
      module.bubbles.push({
        id: id,
        type: options.type
        //additional info
      });
      module.keys[id] = module.bubbles.length - 1;

      //segment container
      var outer = module.flow.append('div')
        .attr('class', 'cb-segment cb-' + options.class + ' cb-bubble-type-' + options.type)
        .attr('id', 'cb-segment-' + id);

      //speaker icon
      outer.append('div').attr('class', 'cb-icon');

      var bubble = outer.append('div')
        .attr('class', 'cb-bubble ' + options.class)
        // .style("height", "50px")
        .append('div')
        .attr('class', 'cb-inner');


      outer.append('hr');

      module.types[options.type](bubble, options, callback);

      module.scrollTo('end');

      return module.ID;
    }
  };

  /**
   * @memberof chatUI
   * @param {d3-selection} bubble - d3 selection of the bubble container
   * @param {object} options - object containing configs {type:'text', class:string ('human' || 'bot'), value:array of objects (e.g. [{label:'yes'}])}
   * @param {function} callback - function to be called after everything is done
   */
  module.types.select = function(bubble, options, callback){
    bubble.selectAll('.cb-choice').data(options.value).enter().append('div')
      .attr('class', 'cb-choice')
      .text(function(d){ return d.label; })
      .on('click', function(d){
        d3.select(this).classed('cb-active', true);
        d3.select(this.parentNode).selectAll('.cb-choice').on('click', function(){});
        callback(d);
      });
  };

  /**
   * @memberof chatUI
   * @param {d3-selection} bubble - d3 selection of the bubble container
   * @param {object} options - object containing configs {type:'text', class:string ('human' || 'bot'), value:string (e.g. 'Hello World')}
   * @param {function} callback - function to be called after everything is done
   */
  module.types.text = function (bubble, options, callback) {
    if (('delay' in options) && options.delay) {
      var animatedCircles = '<div class="circle"></div><div class="circle"></div><div class="circle"></div>';
      bubble.append('div')
        .attr('class', 'cb-waiting')
        .html(animatedCircles);

      setTimeout(function () {

        bubble.select(".cb-waiting").remove();
        module.appendText(bubble, options, callback);

      }, (isNaN(options.delay) ? 1000 : options.delay));
    } else {
      module.appendText(bubble, options, callback);
    }

  };

  /**
   * Helper Function for adding text to a bubble
   * @memberof chatUI
   * @param {d3-selection} bubble - d3 selection of the bubble container
   * @param {object} options - object containing configs {type:'text', class:string ('human' || 'bot'), value:string (e.g. 'Hello World')}
   * @param {function} callback - function to be called after everything is done
   */
  module.appendText = function(bubble, options, callback) {
    bubble.attr('class', 'bubble-ctn-' + options.class).append('p')
      .html(options.value)
      .transition()
      .duration(200)
      .style("width", "auto")
      .style('opacity', 1);

    chat.scrollTo('end');

    callback();
  };

  /**
   * Showing the input module and set cursor into input field
   * @memberof chatUI
   * @param {function} submitCallback - function to be called when user presses enter or submits through the submit-button
   * @param {function} typeCallback - function to when user enters text (on change)
   */
  module.showInput = function (submitCallback, typeCallback) {
    module.inputState = true;

    if (typeCallback) {
      module.input.select('input')
        .on('change', function () {
          typeCallback(d3.select(this).node().value);
        });
    } else {
      module.input.select('input').on('change', function () { });
    }

    module.input.select('input').on('keyup', function () {
        if (d3.event.keyCode == 13) {
          submitCallback(module.input.select('input').node().value);
          module.input.select('input').node().value = '';      
        }
    });

    module.input.select('button')
      .on('click', function () {
        submitCallback(module.input.select('input').node().value);
        module.input.select('input').node().value = '';
      });

    module.input.style('display', 'block');
    module.updateContainer();

    module.input.select('input').node().focus();
    module.scrollTo('end');
  };

  /**
   * Hide the input module
   */
  module.hideInput = function () {
    module.input.select('input').node().blur();
    module.input.style('display', 'none');
    module.inputState = false;
    module.updateContainer();
    module.scrollTo('end');
  };

  /**
   * Remove a bubble from the chat
   * @memberof chatUI
   * @param {integer} id - id of bubble provided by addBubble
   */
  module.removeBubble = function (id) {
    module.flow.select('#cb-segment-' + id).remove();
    module.bubbles.splice(module.keys[id], 1);
    delete module.keys[id];
  };

  /**
   * Remove all bubbles until the bubble with 'id' from the chat
   * @memberof chatUI
   * @param {integer} id - id of bubble provided by addBubble
   */
  module.removeBubbles = function (id) {
    for (var i = module.bubbles.length - 1; i >= module.keys[id]; i--) {
      module.removeBubble(module.bubbles[i].id);
    }
  };

  /**
   * Remove all bubbles until the bubble with 'id' from the chat
   * @memberof chatUI
   * @param {integer} id - id of bubble provided by addBubble
   * @return {object} obj - {el:d3-selection, obj:bubble-data}
   */
  module.getBubble = function (id) {
    return {
      el: module.flow.select('#cb-segment-' + id),
      obj: module.bubbles[module.keys[id]]
    };
  };

  /**
   * Scroll chat flow
   * @memberof chatUI
   * @param {string} position - where to scroll either 'start' or 'end'
   */
  module.scrollTo = function (position) {
    //start
    var s = 0;
    //end
    if (position == 'end') {
      s = module.scroll.property('scrollHeight') - (window.innerHeight-77);
    }
    d3.select('#cb-flow').transition()
      .duration(300)
      .tween("scroll", scrollTween(s));

  };

  function scrollTween(offset) {
    return function () {
      var i = d3.interpolateNumber(module.scroll.property('scrollTop'), offset);
      return function (t) { module.scroll.property('scrollTop', i(t)); };
    };
  }

  function debouncer( func , _timeout ) {
    var timeoutID , timeout = _timeout || 200;
    return function () {
      var scope = this , args = arguments;
      clearTimeout( timeoutID );
      timeoutID = setTimeout( function () {
        func.apply( scope , Array.prototype.slice.call( args ) );
      } , timeout );
    };
  }

  //On Resize scroll to end
  d3.select(window).on('resize', debouncer(function(e){
      module.updateContainer();
  }, 200));

  module.updateContainer();

  return module;
});