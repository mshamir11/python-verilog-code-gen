#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, render_template, request
import logging
from logging import Formatter, FileHandler
from forms import *
import os
from python_utils import ieeconv
import math
#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
app.config.from_object('config')
#db = SQLAlchemy(app)

# Automatically tear down SQLAlchemy.
'''
@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()
'''

# Login required decorator.
'''
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap
'''
#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#


@app.route('/')
def home():
    return render_template('pages/placeholder.home.html')


@app.route('/about')
def about():
    return render_template('pages/placeholder.about.html')


@app.route('/modules')
def modules():
    return render_template('pages/placeholder.module.html')


@app.route('/login')
def login():
    form = LoginForm(request.form)
    return render_template('forms/login.html', form=form)


@app.route('/register')
def register():
    form = RegisterForm(request.form)
    return render_template('forms/register.html', form=form)


@app.route('/forgot')
def forgot():
    form = ForgotForm(request.form)
    return render_template('forms/forgot.html', form=form)

# Error handlers.


@app.errorhandler(500)
def internal_error(error):
    #db_session.rollback()
    return render_template('errors/500.html'), 500


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')


#----------------------------------------------------------------------------#

#----------------------------------------------------------------------------#
# Modules
#----------------------------------------------------------------------------#

# Counters
#----------------------------------------------------------------------------#


# Form
#----------------------------------------------------------------------------#
@app.route('/up-counter-form')
def upcounter_form():
    return render_template('pages/counters/forms/placeholder.upcounter_form.html')

@app.route('/johnson-counter-form')
def johnson_counter_form():
    return render_template('pages/counters/forms/placeholder.johnson_form.html')

@app.route('/ring-counter-form')
def ring_counter_form():
    return render_template('pages/counters/forms/placeholder.ring_form.html')

@app.route('/down-counter-form')
def down_counter_form():
    return render_template('pages/counters/forms/placeholder.down_form.html')

@app.route('/custom-counter-form')
def custom_counter_form():
    return render_template('pages/counters/forms/placeholder.custom_form.html')



@app.route('/up-counter',methods=['POST','GET'])
def upcounter():
    result = request.form
    return render_template('pages/counters/placeholder.upcounter.html',result=result)

@app.route('/johnson-counter',methods=['POST','GET'])
def johnson_counter():   
    result = request.form
    return render_template('pages/counters/placeholder.johnson.html',result=result)

@app.route('/ring-counter',methods=['POST','GET'])
def ring_counter():   
    result = request.form
    return render_template('pages/counters/placeholder.ring.html',result=result)

@app.route('/down-counter',methods=['POST','GET'])
def down_counter():   
    result = request.form
    return render_template('pages/counters/placeholder.down.html',result=result)

@app.route('/custom-counter',methods=['POST','GET'])
def custom_counter():   
    result = request.form
    return render_template('pages/counters/placeholder.custom.html',result=result)


# Flip Flops
#----------------------------------------------------------------------------#

@app.route('/d-flipflop',methods=['POST','GET'])
def d_flipflop():   
    result = request.form
    return render_template('pages/flipflops/placeholder.d_flipflop.html',result=result)

@app.route('/jk-flipflop',methods=['POST','GET'])
def jk_flipflop():   
    result = request.form
    return render_template('pages/flipflops/placeholder.jk_flipflop.html',result=result)

@app.route('/sr-flipflop',methods=['POST','GET'])
def sr_flipflop():   
    result = request.form
    return render_template('pages/flipflops/placeholder.sr_flipflop.html',result=result)

@app.route('/t_flipflop',methods=['POST','GET'])
def t_flipflop():   
    result = request.form
    return render_template('pages/flipflops/placeholder.t_flipflop.html',result=result)


# Registers
#----------------------------------------------------------------------------#

#Forms
#========================================
@app.route('/siso-form')
def siso_form():
    return render_template('pages/registers/forms/placeholder.siso_form.html')

@app.route('/pipo-form')
def pipo_form():
    return render_template('pages/registers/forms/placeholder.pipo_form.html')

@app.route('/piso-form')
def piso_form():
    return render_template('pages/registers/forms/placeholder.piso_form.html')

@app.route('/shiftregister-form')
def shift_register_form():
    return render_template('pages/registers/forms/placeholder.shiftregisters_form.html')

@app.route('/circularregister-form')
def circular_register_form():
    return render_template('pages/registers/forms/placeholder.circularregisters_form.html')



@app.route('/siso',methods=['POST','GET'])
def siso():   
    result = request.form
    return render_template('pages/registers/placeholder.siso.html',result=result)

@app.route('/pipo',methods=['POST','GET'])
def pipo():   
    result = request.form
    return render_template('pages/registers/placeholder.pipo.html',result=result)

@app.route('/piso',methods=['POST','GET'])
def piso():   
    result = request.form
    return render_template('pages/registers/placeholder.piso.html',result=result)

@app.route('/shiftregister',methods=['POST','GET'])
def shiftregister():   
    result = request.form
    return render_template('pages/registers/placeholder.shiftregister.html',result=result)

@app.route('/circularregister',methods=['POST','GET'])
def circularregister():   
    result = request.form
    return render_template('pages/registers/placeholder.circularregister.html',result=result)



#Floating Point Modules
#----------------------------------------------------------------------------#

#Forms
#========================================
@app.route('/floating-adder-form')
def floating_adder_form():
    return render_template('pages/floating_modules/forms/placeholder.floating_adder_form.html')

@app.route('/floating-subtracter-form')
def floating_subtracter_form():
    return render_template('pages/floating_modules/forms/placeholder.floating_subtracter_form.html')

@app.route('/floating-multiplication-form')
def floating_multiplication_form():
    return render_template('pages/floating_modules/forms/placeholder.floating_multiplication_form.html')

@app.route('/floating-division-form')
def floating_division_form():
    return render_template('pages/floating_modules/forms/placeholder.floating_division_form.html')


#========================================
@app.route('/floating-adder',methods=['POST','GET'])
def floating_adder():   
    result = request.form
    sign_bit_a, exp_str_a, mant_str_a = ieeconv.floatingPoint(float(result['bits_a'])) 
    sign_bit_b, exp_str_b, mant_str_b = ieeconv.floatingPoint(float(result['bits_b'])) 
    
    # Final Floating point Representation. 
    ieee_32_a = str(32)+'\'b'+str(sign_bit_a) + '_' + exp_str_a + '_' + mant_str_a
    ieee_32_b = str(32)+'\'b'+str(sign_bit_b) + '_' + exp_str_b + '_' + mant_str_b
    if len(ieee_32_a)>38:
        ieee_32_a = ieee_32_a[:38]
    if len(ieee_32_b)>38:
        ieee_32_b = ieee_32_b[:38]
    iee_dic={}
    iee_dic['a']=ieee_32_a
    iee_dic['b'] = ieee_32_b
    
    return render_template('pages/floating_modules/placeholder.floating_adder.html',result=iee_dic)

@app.route('/floating-subtracter',methods=['POST','GET'])
def floating_subtracter():   
    result = request.form
    sign_bit_a, exp_str_a, mant_str_a = ieeconv.floatingPoint(float(result['bits_a'])) 
    sign_bit_b, exp_str_b, mant_str_b = ieeconv.floatingPoint(float(result['bits_b'])) 
    
    # Final Floating point Representation. 
    ieee_32_a = str(32)+'\'b'+str(sign_bit_a) + '_' + exp_str_a + '_' + mant_str_a
    ieee_32_b = str(32)+'\'b'+str(sign_bit_b) + '_' + exp_str_b + '_' + mant_str_b
    if len(ieee_32_a)>38:
        ieee_32_a = ieee_32_a[:38]
    if len(ieee_32_b)>38:
        ieee_32_b = ieee_32_b[:38]
    iee_dic={}
    iee_dic['a']=ieee_32_a
    iee_dic['b'] = ieee_32_b
    
    
    return render_template('pages/floating_modules/placeholder.floating_subtracter.html',result=iee_dic)

@app.route('/floating-multiplication',methods=['POST','GET'])
def floating_multiplication():   
    result = request.form
    sign_bit_a, exp_str_a, mant_str_a = ieeconv.floatingPoint(float(result['bits_a'])) 
    sign_bit_b, exp_str_b, mant_str_b = ieeconv.floatingPoint(float(result['bits_b'])) 
    
    # Final Floating point Representation. 
    ieee_32_a = str(32)+'\'b'+str(sign_bit_a) + '_' + exp_str_a + '_' + mant_str_a
    ieee_32_b = str(32)+'\'b'+str(sign_bit_b) + '_' + exp_str_b + '_' + mant_str_b
    if len(ieee_32_a)>38:
        ieee_32_a = ieee_32_a[:38]
    if len(ieee_32_b)>38:
        ieee_32_b = ieee_32_b[:38]
    iee_dic={}
    iee_dic['a']=ieee_32_a
    iee_dic['b'] = ieee_32_b
    return render_template('pages/floating_modules/placeholder.floating_multiplication.html',result=iee_dic)

@app.route('/floating-division',methods=['POST','GET'])
def floating_division():   
    result = request.form
    sign_bit_a, exp_str_a, mant_str_a = ieeconv.floatingPoint(float(result['bits_a'])) 
    sign_bit_b, exp_str_b, mant_str_b = ieeconv.floatingPoint(float(result['bits_b'])) 
    
    # Final Floating point Representation. 
    ieee_32_a = str(32)+'\'b'+str(sign_bit_a) + '_' + exp_str_a + '_' + mant_str_a
    ieee_32_b = str(32)+'\'b'+str(sign_bit_b) + '_' + exp_str_b + '_' + mant_str_b
    if len(ieee_32_a)>38:
         ieee_32_a = ieee_32_a[:38]
    if len(ieee_32_b)>38:
        ieee_32_b = ieee_32_b[:38]
    iee_dic={}
    iee_dic['a']=ieee_32_a
    iee_dic['b'] = ieee_32_b
    return render_template('pages/floating_modules/placeholder.floating_division.html',result=iee_dic)
# FSM
#----------------------------------------------------------------------------#

#Forms
#========================================



@app.route('/fsm-moore-form')
def fsm_moore_form():
    return render_template('pages/fsm/forms/placeholder.moore_form.html')


@app.route('/fsm-moore',methods=['POST','GET'])
def fsm_moore():   
    result = request.form
    result_dic =result.to_dict(flat=False)
    print(result_dic)
    log_count = math.log2(len(result_dic['present']))
    if log_count != int(log_count):
        log_count=int(log_count)+1
    else:
        log_count = int(log_count)
    return render_template('pages/fsm/placeholder.moore.html',result=result_dic,count=log_count)



@app.route('/fsm-mealy-form')
def fsm_mealey_form():
    return render_template('pages/fsm/forms/placeholder.mealey_form.html')


@app.route('/fsm-mealy',methods=['POST','GET'])
def fsm_mealey():   
    result = request.form
    result_dic =result.to_dict(flat=False)
    log_count = math.log2(len(result_dic['present']))
    if log_count != int(log_count):
        log_count=int(log_count)+1
    else:
        log_count = int(log_count)
    print(log_count)
    return render_template('pages/fsm/placeholder.mealey.html',result=result_dic,count=log_count)
#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
