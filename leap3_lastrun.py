#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on Fri Nov 10 13:18:42 2023
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.5'
expName = 'leap3'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s' % (expInfo['participant'], expName)

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/maddie/Library/CloudStorage/Box-Box/LEAP/version3/leap3_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1512, 982], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color='white', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "init" ---
# Run 'Begin Experiment' code from setup
import random
import math

# define random function
def randomizer(x,seed=None):
  random.seed(seed)
  for i in reversed(range(1,len(x))):
    j = math.floor(random.random() * (i +1))
    x[i], x[j] = x[j], x[i]
  return(x)

# defining variables
ntrials = 30 # number of trials per block
subNum = int(expInfo['participant'])
nBlocks = 40
nTargets = 20
if subNum %2 == 0:
    hDemandLoc = 'upper'
    lDemandLoc = 'lower'
else:
    hDemandLoc = 'lower'
    lDemandLoc = 'upper'

# Set up practice blocks
nPracBlock = 2
nPracTrials = 14
pracWords = ['umpire','tricycle','slumber','grimace','unscrew','summary','sponsor','overshoot','reputable','infinity','revival','picture','busted','hiring']
pracNonwords = ['alolition', 'julled','lumbigo','lurshing','raestro','hasking','latador','treeps','crinklo','grocus','trotch','grutch','turative','curlecs']
pracWords = randomizer(pracWords)
pracNonwords = randomizer(pracNonwords)

pracStim= []
pracWordType = []
pracCorrKey = []
for b in list(range(0,nPracBlock)):
    pS = pracWords[(b*int(nPracTrials/2)):((b+1)*int(nPracTrials/2))] + pracNonwords[(b*int(nPracTrials/2)):((b+1)*int(nPracTrials/2))]
    pWT = ['w']*int(nPracTrials/2) + ['nw']*int(nPracTrials/2)
    pCK = ['g']*int(nPracTrials/2) + ['h']*int(nPracTrials/2)
    pS= randomizer(pS, seed = subNum)
    pWT = randomizer(pWT, seed = subNum)
    pCK = randomizer(pCK, seed = subNum)
    pracStim.append(pS)
    pracWordType.append(pWT)
    pracCorrKey.append(pCK)

# set word lists
words = ['supplier', 'govern', 'deceit', 'scatter', 'forgery', 'abhorrent', 'cookbook', 'protest', 'colored', 'pressures', 'pollute', 'rational', 'army', 'punctual', 'strenuous', 'dreaded', 'angry', 'destroy', 'senior', 'pillage', 'handcuff', 'inducing', 'rewrite', 'icepick', 'female', 'infusion', 'sunshine', 'turning', 'combat', 'lawsuit', 'triangle', 'suburb', 'catacomb', 'maiden', 'comply', 'divider', 'ignore', 'nostril', 'regional', 'threaded', 'orange', 'deadly', 'solidity', 'dominion', 'castaway', 'oppose', 'alchemist', 'showdown', 'treason', 'intrude', 'perishing', 'demise', 'previous', 'uncounted', 'footstep', 'tablet', 'eyesight', 'latter', 'permeable', 'butler', 'aqueduct', 'vaporize', 'digest', 'foster', 'image', 'crazy', 'virulent', 'recollect', 'forbid', 'reason', 'nature', 'hustle', 'teamwork', 'caloric', 'violate', 'emergence', 'collision', 'buzzer', 'swatches', 'heaviest', 'admire', 'century', 'legalize', 'unspoken', 'regards', 'armada', 'command', 'companion', 'organize', 'engineer', 'forecast', 'condensed', 'throttle', 'blueberry', 'fetching', 'vented', 'brighten', 'attract', 'frequency', 'publish', 'party', 'euphoric', 'deficit', 'module', 'awful', 'ignoble', 'standard', 'garment', 'populace', 'achieve', 'remover', 'warmer', 'criminal', 'talent', 'ahead', 'bloodless', 'amaze', 'checkout', 'lentils', 'burrowing', 'probable', 'fillings', 'describe', 'unbridled', 'earnest', 'servant', 'gallon', 'record', 'burning', 'culinary', 'manage', 'regiment', 'mopping', 'unmarked', 'penalize', 'lifetime', 'prison', 'pretzel', 'practice', 'reconcile', 'moral', 'tycoon', 'envelop', 'stable', 'outflow', 'cervical', 'disease', 'expensive', 'plunging', 'afford', 'failure', 'slogan', 'inversion', 'uncorked', 'design', 'realize', 'rivet', 'fictional', 'defeat', 'coverall', 'column', 'painter', 'glassware', 'entropy', 'located', 'season', 'flicking', 'pressing', 'outrank', 'bedding', 'encounter', 'rawhide', 'mitten', 'roughly', 'childhood', 'outset', 'remade', 'hangar', 'rejoiced', 'explosion', 'skiing', 'insertion', 'patio', 'committed', 'acorn', 'finish', 'railroad', 'region', 'usage', 'entitle', 'delegate', 'postal', 'artifact', 'fidelity', 'epic', 'micron', 'sliding', 'couple', 'pepperoni', 'remain', 'advantage', 'potter', 'tipoff', 'affluent', 'exclusion', 'removable', 'derived', 'befriend', 'aligning', 'parent', 'jiggling', 'visible', 'rodeo', 'renown', 'elderly', 'expounded', 'usually', 'audience', 'attended', 'retain', 'loneliest', 'railway', 'assent', 'casino', 'decant', 'incorrect', 'enabled', 'implode', 'marinate', 'bullet', 'correct', 'stagger', 'forfeit', 'medium', 'landing', 'equitable', 'ergonomic', 'monopoly', 'unlined', 'ensues', 'happen', 'antique', 'cutout', 'meteoroid', 'issue', 'resonant', 'efficient', 'fragment', 'student', 'splatter', 'entertain', 'stalemate', 'measure', 'midday', 'kickoff', 'fission', 'hatred', 'reborn', 'primal', 'country', 'dishwater', 'mandate', 'create', 'knowledge', 'thesis', 'calcify', 'insole', 'sequence', 'holdup', 'pester', 'sequence', 'permute', 'oppose', 'contain', 'relaying', 'seldom', 'scarlet', 'vibrate', 'moisture', 'decency', 'turntable', 'dabble', 'giving', 'recount', 'managed', 'exploit', 'tragedy', 'enunciate', 'jungle', 'venturous', 'aviation', 'rudder', 'paying', 'resume', 'outfit', 'arrive', 'analysis', 'maximized', 'hardest', 'machinery', 'grieving', 'humanize', 'wrestle', 'larger', 'retreat', 'figure', 'massacre', 'cherry', 'disperse', 'dentures', 'urgent', 'laser', 'owner', 'ascending', 'cavern', 'repayment', 'irregular', 'innocent', 'vinegar', 'trembles', 'cessation', 'even', 'argue', 'minimum', 'potent', 'curricula', 'listless', 'rationale', 'upstairs', 'dealer', 'arrival', 'handed', 'helpful', 'phonology', 'guitar', 'infancy', 'picnic', 'volition', 'fallacy', 'stranded', 'alarm', 'terrify', 'obtuse', 'index', 'consonant', 'system', 'rainfall', 'blocking', 'dialect', 'whirlpool', 'summon', 'curtail', 'actual', 'prohibit', 'baseline', 'telecast', 'glamorous', 'unversed', 'except', 'martial', 'series', 'surfaced', 'undertake', 'mixture', 'inverted', 'agony', 'statute', 'sonnet', 'suspect', 'observer', 'number', 'intersect', 'emotion', 'asthmatic', 'lofty', 'filter', 'perform', 'omission', 'bypassed', 'arbitrary', 'preserve', 'overwork', 'movie', 'vivid', 'robbery', 'charcoal', 'company', 'suddenly', 'urgency', 'ulcer', 'gymnasium', 'potatoes', 'actively', 'expired', 'antonym', 'minister', 'terming', 'miracle', 'abstain', 'computer', 'nameplate', 'tinker', 'other', 'intended', 'bookend', 'staircase', 'saturate', 'overflow', 'kettle', 'encrusted', 'official', 'handle', 'walnut', 'obviously', 'digested', 'uncle', 'ordinary', 'butcher', 'levels', 'dialogues', 'rearrange', 'presently', 'matter', 'paranoid', 'itself', 'emission', 'require', 'satisfies', 'enacted', 'spaceship', 'warden', 'hangar', 'harmful', 'formation', 'standard', 'absent', 'inside', 'mystery', 'extend', 'mortgage', 'compose', 'volume', 'slightly', 'seeming', 'anterior', 'static', 'gaining', 'stooping', 'booster', 'saucer', 'classify', 'single', 'shivering', 'stretches', 'partner', 'arrested', 'release', 'surround', 'desert', 'marvel', 'anonymous', 'exemplify', 'cabinet', 'addition', 'amplifier', 'result', 'truthful', 'bother', 'anemic', 'professor', 'whirling', 'stifle', 'acoustic', 'embrace', 'twenties', 'coupling', 'trooper', 'sputter', 'buttress', 'reprint', 'deeper', 'maintain', 'duplex', 'colicky', 'purport', 'distrust', 'arrow', 'optional', 'shamrock', 'sustain', 'subpoena', 'handbook', 'target', 'personify', 'category', 'triplet', 'parody', 'preclude', 'living', 'diatonic', 'courier', 'reforest', 'boutique', 'despise', 'ready', 'afternoon', 'sullen', 'rocket', 'expected', 'forgive', 'illness', 'widely', 'exit', 'bickering', 'disuse', 'trophy', 'serving', 'gazes', 'religious', 'mullet', 'border', 'extruded', 'brother', 'prominent', 'seasoning', 'melodic', 'budget', 'resent', 'become', 'sweeping', 'demon', 'daylight', 'cassette', 'caution', 'causality', 'boulder', 'shockwave', 'function', 'leather', 'restock', 'arranged', 'cobalt', 'rarely', 'amidst', 'graveyard', 'calming', 'bamboo', 'purpose', 'corduroy', 'revising', 'define', 'airline', 'noblest', 'chemical', 'dehydrate', 'educate', 'binder', 'presence', 'deserve', 'harder', 'confined', 'comment', 'sampling', 'planar', 'undue', 'pocket', 'overcoat', 'hotplate', 'mounting', 'acidic', 'apology', 'maroon', 'rapport', 'pariah', 'intercede', 'halter', 'oldest', 'axis', 'ethical', 'accessory', 'submit', 'goblet', 'tucker', 'hindsight', 'acting', 'carnival', 'surface', 'typical', 'contact', 'tracing', 'fracture', 'mining', 'infested', 'posing', 'hubris', 'airmen', 'provide', 'superstar', 'integral', 'persona']
words = randomizer(words, seed = subNum)
nonwords = ['cogantly', 'chight', 'doads', 'nimp', 'downtrund', 'alomalous', 'rootsie', 'omners', 'coster', 'cripet', 'tyena', 'arrigns', 'ireology', 'rumblos', 'apticle', 'lutton', 'glaims', 'nelvet', 'etber', 'havel', 'thamp', 'deakers', 'smolvers', 'bumbo', 'drine', 'wienegs', 'imprives', 'brongs', 'congraks', 'pypecast', 'glates', 'browting', 'ezulated', 'trises', 'borrent', 'fudden', 'corg', 'poyride', 'soluced', 'decantel', 'slears', 'eightiech', 'chiffol', 'neuran', 'carony', 'joadbed', 'veirs', 'tharcely', 'nollow', 'mabit', 'neliefs', 'pegend', 'ringlat', 'bropic', 'glattery', 'harfing', 'bamps', 'houted', 'pexts', 'quickel', 'buaint', 'volder', 'hinsome', 'gelfry', 'culer', 'miability', 'dorte', 'alticles', 'smallash', 'zears', 'lenie', 'flougy', 'uncarled', 'donastic', 'brouhuha', 'asclibed', 'shillac', 'duries', 'greft', 'aicline', 'fabstand', 'sheerio', 'nimono', 'antwers', 'ounside', 'germeated', 'contund', 'misobeyed', 'derisury', 'tunneg', 'geborn', 'breiled', 'geissue', 'lecked', 'gumdrep', 'sprea', 'clume', 'puggers', 'rualify', 'erithets', 'fraft', 'mogus', 'fuack', 'withep', 'preight', 'nearsipe', 'senalize', 'ganter', 'mebase', 'cooray', 'rasuals', 'gerby', 'dricked', 'bentler', 'lonnote', 'scrooner', 'doxing', 'spiud', 'neally', 'ufionize', 'digar', 'irfirm', 'mosary', 'elvisages', 'stuggard', 'fashing', 'serfume', 'fallint', 'ements', 'miurnal', 'hutting', 'rarren', 'crimb', 'slending', 'drauns', 'ludictous', 'pastnoss', 'tenpince', 'huests', 'efcorted', 'gensions', 'arcients', 'gestalion', 'seighing', 'aefated', 'chonemic', 'sazer', 'lightels', 'seartfelt', 'gablus', 'detrabe', 'gures', 'endgume', 'prillway', 'temelity', 'padicals', 'talate', 'gackpedal', 'shests', 'halms', 'walsams', 'scrib', 'yearnungs', 'porghum', 'gelented', 'refebs', 'numbled', 'dingly', 'bailmenz', 'phraining', 'iflaid', 'thaken', 'treenery', 'finstrel', 'pircus', 'frose', 'plapping', 'pranny', 'rangel', 'crundle', 'puyer', 'gontracts', 'collute', 'peems', 'gaioty', 'pallir', 'sording', 'funtair', 'plymie', 'brials', 'abraid', 'lasprey', 'golemic', 'setwixt', 'hasks', 'drobate', 'dileting', 'huzzles', 'hackal', 'olgies', 'ralliep', 'welayed', 'trocess', 'poars', 'profats', 'sarlock', 'ifling', 'spigat', 'snocks', 'troven', 'yash', 'kiner', 'yellep', 'theery', 'nomma', 'flooted', 'brimitar', 'draze', 'clattest', 'dazid', 'glocked', 'sludding', 'pimorous', 'reddar', 'sporidic', 'fards', 'ragtam', 'grolific', 'beartiset', 'begut', 'bengths', 'sponto', 'pripend', 'ifkling', 'prama', 'nogwhell', 'plartly', 'hostade', 'elormity', 'goltish', 'wimpid', 'cegalia', 'newstrint', 'acroad', 'frunted', 'worps', 'egect', 'itfidels', 'runabouk', 'addma', 'misest', 'aggepting', 'noils', 'gepealed', 'latirizes', 'trembla', 'prame', 'ucility', 'frader', 'praiged', 'tinion', 'trake', 'blerapies', 'imotope', 'opert', 'carbled', 'peadgear', 'plashed', 'tredits', 'geadpan', 'cemoir', 'guffy', 'labitable', 'slooping', 'brimitive', 'ounwit', 'hecture', 'attrove', 'hemoter', 'moyeur', 'snife', 'teliever', 'pamine', 'vopings', 'lancos', 'pleamed', 'adok', 'baults', 'bluads', 'ronic', 'razelle', 'airbis', 'maunches', 'egcused', 'ephically', 'mandlers', 'dounger', 'noblin', 'rowel', 'defensa', 'pracking', 'unamufed', 'befin', 'oleandur', 'squadroim', 'gradielts', 'grenavier', 'recipus', 'legalosm', 'ghists', 'brudent', 'sonkers', 'elalt', 'trecious', 'batire', 'hodels', 'tibs', 'sefraud', 'fuestion', 'blanned', 'birn', 'subber', 'tritical', 'slutches', 'crudios', 'natch', 'roodies', 'ilcurring', 'mustled', 'sefine', 'quittint', 'gairs', 'gounts', 'markot', 'wrecber', 'reses', 'gewer', 'dests', 'butled', 'halents', 'rebool', 'etuip', 'oalis', 'hanling', 'ugifies', 'filny', 'eugenifs', 'bellicove', 'mantos', 'horks', 'daining', 'ronvince', 'snays', 'eaglot', 'unstatle', 'gettle', 'guivers', 'togglo', 'fuintets', 'ilterfere', 'amkles', 'fivalve', 'fuhrek', 'gremieres', 'farochial', 'thrapping', 'cartles', 'ebciting', 'fomrade', 'kraums', 'offonents', 'metebing', 'amms', 'grefab', 'otoist', 'valif', 'outlaved', 'athcan', 'ebuating', 'slimped', 'tiery', 'parlayid', 'lignpost', 'portify', 'graciap', 'bureaug', 'latpin', 'gigglod', 'currowing', 'vergas', 'pived', 'sodent', 'vorm', 'twarfs', 'epthuse', 'shimble', 'ecistle', 'heuls', 'glating', 'fomes', 'moozy', 'snorls', 'apop', 'chraps', 'sunhess', 'brank', 'mitro', 'atabaster', 'gund', 'gonesty', 'schides', 'chone', 'fassed', 'unwose', 'ipiocy', 'unburnid', 'flieves', 'miteous', 'cayward', 'favoting', 'theles', 'riosk', 'dusmy', 'rantho', 'loached', 'grested', 'galashes', 'splum', 'sopes', 'inforl', 'prawls', 'stelled', 'tasher', 'smabled', 'peags', 'oginous', 'rander', 'graiking', 'lanthers', 'jinds', 'gunrunker', 'shurk', 'urique', 'clypaper', 'esdings', 'dontrite', 'ebince', 'elpired', 'eggays', 'clarms', 'fullity', 'huffle', 'slooch', 'vintnel', 'blipover', 'churnad', 'pakened', 'fonducts', 'bingu', 'lavilion', 'fravity', 'unrealon', 'joses', 'tusied', 'mennel', 'rillains', 'chesume', 'susher', 'ameld', 'veranpah', 'haurded', 'atble', 'felevance', 'kilotin', 'chrik', 'greakable', 'frigs', 'tining', 'dorth', 'frogmy', 'selongs', 'ottans', 'splinging', 'ubefully', 'tapling', 'olerates', 'phambled', 'pregs', 'surdens', 'plogging', 'sength', 'impirt', 'unsmilung', 'dariner', 'pender', 'topefuls', 'egpended', 'hivinity', 'redefloy', 'catgup', 'blassed', 'rascaps', 'podges', 'clooped', 'gigoho', 'lindo', 'edasion', 'sorping', 'podes', 'cheathe', 'chining', 'bulmed', 'erlighten', 'mubby', 'menarthe', 'incidonts', 'mestowal', 'chappef', 'odacles', 'thacked', 'dislokes', 'earmaff', 'ofsters', 'lovud', 'scabry', 'paterways', 'shazer', 'contusiok', 'earterner', 'trewl', 'beggarlan', 'tuckel', 'godomy', 'poughest', 'traze', 'balign', 'ausht', 'nopping', 'naxis', 'racile', 'undimmec', 'facienda', 'bloves', 'ciping', 'dredigest', 'etcess', 'priant', 'roaned', 'sooled', 'peanimate', 'appain', 'alber', 'flacked', 'elpousal', 'louches', 'trallion', 'chyme', 'atch', 'nores', 'fisco', 'elbalm', 'scack', 'metrol', 'peahem', 'otiates', 'pammed', 'nauling', 'mamps', 'chrayed', 'thorifies', 'scrobby', 'baladroit', 'grummer', 'leuter', 'mineluyer', 'pigned', 'hegacy', 'retona', 'migmarole', 'capobly', 'reloant', 'slowning', 'fatho', 'dumult', 'huntry', 'sengry', 'cills', 'iolize', 'bettled', 'passet', 'allained', 'glapula', 'schinter', 'arpired', 'igiom', 'atsless', 'planofoad', 'frowsed', 'erony', 'veclors']
nonwords = randomizer(nonwords, seed = subNum)
targets = ['giraffe','monkey','chicken','elephant','butterfly','flamingo','dolphin','spider','octopus','ladybug','crocodile','kangaroo','rabbit','porcupine','gorilla','jaguar','coyote','caterpillar','lizard','squirrel']

tarWordType = ['w']*int(len(targets))
targets = randomizer(targets, seed = subNum)
# 1 = high demand, target
# 2 = high demand, no target
# 3 = low demand, no target
# 4 = low demand, target
blockOrder = []
for n in [1,2,3,4]:
  random_order = randomizer([1,1,1,1,2,3,3,3,3,4], seed = subNum)
  blockOrder = blockOrder + random_order
  
# Randmoize stimuli and conditions
block = []
stim = []
blockType = []
role = []
wordType = []
correctKey = []
stimLocation = []
blockDesc = []
for i in list(range(0,nBlocks)):
  block.append([i] * ntrials)
  seed = subNum*(i+1)
  b = blockOrder[i]
  targetTrial = random.randint(9,29)
  this_stim = words[i*int(ntrials/2):(i+1)*int(ntrials/2)] + nonwords[i*int(ntrials/2):(i+1)*int(ntrials/2)]
  this_role = ['w']*int(ntrials/2) + ['nw'] * int(ntrials/2)
  this_wordType = ['w']*int(ntrials/2) + ['nw'] * int(ntrials/2)
  this_correctKey = ['g'] * int(ntrials/2) + ['h'] * int(ntrials/2)
  this_stim = randomizer(this_stim, seed = seed)
  this_role = randomizer(this_role, seed = seed)
  this_wordType = randomizer(this_wordType, seed = seed)
  this_correctKey = randomizer(this_correctKey, seed = seed)
  if b == 1:
    this_blockDesc = ['HiDemTar']*ntrials
    this_stimLocation = [hDemandLoc] * ntrials
    this_stim[targetTrial] = targets[0]
    this_role[targetTrial:targetTrial+3] = ['target','aftertar1','aftertar2','aftertar3']
    this_wordType[targetTrial] = 'target'
    this_correctKey[targetTrial] = 'q'
    targets = targets[1:len(targets)]
  if b == 2:
    this_blockDesc = ['HiDemNoTar'] * ntrials
    this_stimLocation = [hDemandLoc] * ntrials
  if b == 3:
    this_blockDesc = ['LoDemNoTar'] * ntrials
    this_stimLocation = [lDemandLoc] * ntrials
  if b == 4:
    this_blockDesc = ['LoDemTar'] * ntrials
    this_stimLocation = [lDemandLoc] * ntrials
    this_stim[targetTrial] = targets[0]
    this_role[targetTrial:targetTrial+3] = ['target','aftertar1','aftertar2','aftertar3']
    this_wordType[targetTrial] = 'target'
    this_correctKey[targetTrial] = 'q'
    targets = targets[1:len(targets)]

  blockType.append([b] * ntrials)
  blockDesc.append(this_blockDesc)
  stim.append(this_stim)
  role.append(this_role)
  wordType.append(this_wordType)
  correctKey.append(this_correctKey)
  stimLocation.append(this_stimLocation)


# --- Initialize components for Routine "welcome" ---
welcomeText = visual.TextStim(win=win, name='welcomeText',
    text='Welcome to the experiment!\n\n\nWhen you are ready to begin, press ENTER.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=1.2, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
welcomeKey = keyboard.Keyboard()

# --- Initialize components for Routine "demo1Inst" ---
demo1InstText = visual.TextStim(win=win, name='demo1InstText',
    text='Before we get started with the task, we would like you to answer a few questions about yourself.\n\nPress ENTER to continue.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=1.2, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
demoInstTextKey = keyboard.Keyboard()

# --- Initialize components for Routine "demoAge" ---
ageText = visual.TextStim(win=win, name='ageText',
    text='How old are you? Please type your answer.',
    font='Arial',
    pos=(0, .15), height=0.05, wrapWidth=1.2, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
ageTextbox = visual.TextBox2(
     win, text=None, font='Arial',
     pos=(0, 0),     letterHeight=0.05,
     size=(0.5, 0.1), borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor='black',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='ageTextbox',
     autoLog=True,
)
ageNextText = visual.TextStim(win=win, name='ageNextText',
    text='Press SPACE to submit response.',
    font='Arial',
    pos=(0, -.15), height=0.05, wrapWidth=1.2, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
ageNextKey = keyboard.Keyboard()

# --- Initialize components for Routine "demoGender" ---
genderText = visual.TextStim(win=win, name='genderText',
    text='What is your gender? Please type your answer. Leave blank if you prefer not to answer.',
    font='Arial',
    pos=(0, 0.15), height=0.05, wrapWidth=1.2, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
genderTextbox = visual.TextBox2(
     win, text=None, font='Arial',
     pos=(0, 0),     letterHeight=0.05,
     size=(0.5, 0.1), borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor='black',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='genderTextbox',
     autoLog=True,
)
genderNextText = visual.TextStim(win=win, name='genderNextText',
    text='Press ENTER to submit your response.',
    font='Arial',
    pos=(0, -0.15), height=0.05, wrapWidth=1.2, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
genderNextKey = keyboard.Keyboard()

# --- Initialize components for Routine "demoRace_init" ---

# --- Initialize components for Routine "demoRace" ---
raceText = visual.TextStim(win=win, name='raceText',
    text='',
    font='Arial',
    pos=(0, 0.15), height=0.05, wrapWidth=1.2, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
raceOpts = visual.TextStim(win=win, name='raceOpts',
    text='If yes, press "y".\nIf no, press "n".\n\nPress "x" if you prefer not to answer.',
    font='Arial',
    pos=(0, -0.05), height=0.05, wrapWidth=1.2, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
raceResp = keyboard.Keyboard()

# --- Initialize components for Routine "LDTreread" ---
LDTrereadText = visual.TextStim(win=win, name='LDTrereadText',
    text='Please re-read through the instructions.\n\nPress ENTER to continue.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
LDTrereadKey = keyboard.Keyboard()

# --- Initialize components for Routine "LDTInst1" ---
LDTInst1Text = visual.TextStim(win=win, name='LDTInst1Text',
    text='Great, now you will continue to the task.\n\nIn this study, we are investigating the speed with which certain words and syllables are processed. Your task is to indicate whether or not a string of letters forms a real word.\n\nWhen you encounter a real word, press "g". When you encounter a string of letters that is not a real word, press "h".\n\n\nPress "g" to continue with the instrucitons.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=1.2, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
LDTInst1Key = keyboard.Keyboard()

# --- Initialize components for Routine "LDTInst2" ---
LDTInst2Text = visual.TextStim(win=win, name='LDTInst2Text',
    text='This is called the SPEED task because the goal is to respond as quickly as possible. Therefore, you should try to respond as soon as you can without sacrificing accuracy. Your goal should be to respond in less than one second. The strings of letters are presented in random order, so do not try to predict the upcoming string of letters; that will only slow you down.\n\n\nPress ENTER to proceed.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=1.2, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
LDTInst2Key = keyboard.Keyboard()

# --- Initialize components for Routine "LDTInst3" ---
LDTInst3Text = visual.TextStim(win=win, name='LDTInst3Text',
    text='The SPEED task will be broken down into segments. During each segment, you will complete a series of SPEED trials before receiving a short break. In some segments, the strings of letters will appear in the upper part of the screen. In other segments, the strings of letters will appear in the lower part of the screen. A "+"  will appear on the screen before the string of letters appears. This is your fixation point, which indicates where the string of letters will appear. After your response is made, you will be given a very brief break before the next fixation point appears.\n\nPress SPACE to proceed.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=1.2, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
LDTInst3Key = keyboard.Keyboard()

# --- Initialize components for Routine "LDTcheck" ---
LDTcheckText = visual.TextStim(win=win, name='LDTcheckText',
    text='Do you understand these instructions?\n\nIf yes, press "y".\nIf no, press "n".',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
LDTcheckKey = keyboard.Keyboard()

# --- Initialize components for Routine "LDTInst5" ---
LDTInst5Text = visual.TextStim(win=win, name='LDTInst5Text',
    text='Try a few for practice. In the practice trials, you will be given feedback on the accuracy and speed of your response. Try to speed up your response as much as possible without significantly sacrificing accuracy. It is normal to misjudge a few of the words.\n\n\nPress ENTER to practice the SPEED task.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=1.2, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
LDTInst5Key = keyboard.Keyboard()

# --- Initialize components for Routine "countdown" ---
five = visual.TextStim(win=win, name='five',
    text='5',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
four = visual.TextStim(win=win, name='four',
    text='4',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
three = visual.TextStim(win=win, name='three',
    text='3',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
two = visual.TextStim(win=win, name='two',
    text='2',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
one = visual.TextStim(win=win, name='one',
    text='1',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "pracBlockinit" ---

# --- Initialize components for Routine "pracTrialinit" ---

# --- Initialize components for Routine "pracfix500" ---
fixcross = visual.ShapeStim(
    win=win, name='fixcross', vertices='cross',
    size=(0.05, 0.05),
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=0.01,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=0.0, interpolate=True)

# --- Initialize components for Routine "LDTprac" ---
LDTpracWord = visual.TextStim(win=win, name='LDTpracWord',
    text='',
    font='Arial',
    pos=[0,0], height=0.075, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
LDTpracKey = keyboard.Keyboard()

# --- Initialize components for Routine "pracFeedback" ---
LDTpracFeedback = visual.TextStim(win=win, name='LDTpracFeedback',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "pracBreak" ---
pracBreakText = visual.TextStim(win=win, name='pracBreakText',
    text='Break!\n\nThe next segment will begin in 5 seconds.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "pracCountdown" ---
fiveText = visual.TextStim(win=win, name='fiveText',
    text='5',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
fourText = visual.TextStim(win=win, name='fourText',
    text='4',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
threeText = visual.TextStim(win=win, name='threeText',
    text='3',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
twoText = visual.TextStim(win=win, name='twoText',
    text='2',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
oneText = visual.TextStim(win=win, name='oneText',
    text='1',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# --- Initialize components for Routine "PMreread" ---
PMrereadtext = visual.TextStim(win=win, name='PMrereadtext',
    text='Please re-read the instructions.\n\nPress ENTER to continue.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
PMrereadKey = keyboard.Keyboard()

# --- Initialize components for Routine "PMinst1" ---
PMinstBackground = visual.Rect(
    win=win, name='PMinstBackground',
    width=(2, 2)[0], height=(2, 2)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='blue', fillColor='blue',
    opacity=None, depth=0.0, interpolate=True)
pmInst1Text = visual.TextStim(win=win, name='pmInst1Text',
    text='--- PLEASE READ CAREFULLY ---\n\nIn this experiment, we are interested in your ability to perform an action at a given point in the future. Therefore, during the SPEED task, we would like you to perform a special action whenever the word on the screen is an animal. Here are two examples:\n\ncheetah            hamster\n\nWhenever the word on the screen is an animal, we would like you to press the "q" key. If you forget to press "q" right away, you may do so as soon as you remember. \n\nPress "q" to proceed.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=1.2, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
PMinst1Key = keyboard.Keyboard()

# --- Initialize components for Routine "PMinst2" ---
PMinst2Text = visual.TextStim(win=win, name='PMinst2Text',
    text='Although you will still be making word and nonword judgements, your primary task is to press "q" when you see an animal appear on the screen.\n\nPress ENTER to continue.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=1.2, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
PMinst2Key = keyboard.Keyboard()

# --- Initialize components for Routine "PMcheck" ---
PMcheckText = visual.TextStim(win=win, name='PMcheckText',
    text='Do you understand these instructions?\n\nIf yes, press "y".\nIf no, press "n".',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
PMcheckKey = keyboard.Keyboard()

# --- Initialize components for Routine "PMcue" ---
cueText = visual.TextStim(win=win, name='cueText',
    text='What is the type of word you should be looking for?',
    font='Arial',
    pos=(0, 0.15), height=0.05, wrapWidth=1.2, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
cueTextbox = visual.TextBox2(
     win, text=None, font='Arial',
     pos=(0, 0),     letterHeight=0.05,
     size=(0.5, 0.1), borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor='black',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='cueTextbox',
     autoLog=True,
)
cueNextKey = keyboard.Keyboard()
cueNextText = visual.TextStim(win=win, name='cueNextText',
    text='Press ENTER to submit your response.',
    font='Arial',
    pos=(0, -0.15), height=0.05, wrapWidth=1.2, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "PMintention" ---
intentionText = visual.TextStim(win=win, name='intentionText',
    text='What is the button you should press when you see that word type?',
    font='Arial',
    pos=(0, 0.15), height=0.05, wrapWidth=1.2, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
intentionTextbox = visual.TextBox2(
     win, text=None, font='Arial',
     pos=(0, 0),     letterHeight=0.05,
     size=(0.5, 0.1), borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor='black',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='intentionTextbox',
     autoLog=True,
)
intentionNextKey = keyboard.Keyboard()
intentionNextText = visual.TextStim(win=win, name='intentionNextText',
    text='Press SPACE to submit your response.',
    font='Arial',
    pos=(0, -0.15), height=0.05, wrapWidth=1.2, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "LDTbegin1" ---
begin1Text = visual.TextStim(win=win, name='begin1Text',
    text='Great, now you are ready to begin the SPEED task. \n\nAs a reminder, you should press "g" if the string of letters on the screen is a real word and "h" if it is not a word. Importantly, if the string of letters on the screen is an animal, you should press "q".\n\nYou\'re primary goal is to press "q" if you see an animal.\n\nPress "q" to continue.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=1.2, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
begin1Key = keyboard.Keyboard()

# --- Initialize components for Routine "LDTbegin2" ---
begin2Text = visual.TextStim(win=win, name='begin2Text',
    text='The remaining SPEED task is somewhat taxing. Please do your best to stay focused throughout.\n\nPress ENTER to start the SPEED task.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=1.2, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
begin2Key = keyboard.Keyboard()

# --- Initialize components for Routine "countdown" ---
five = visual.TextStim(win=win, name='five',
    text='5',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
four = visual.TextStim(win=win, name='four',
    text='4',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
three = visual.TextStim(win=win, name='three',
    text='3',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
two = visual.TextStim(win=win, name='two',
    text='2',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
one = visual.TextStim(win=win, name='one',
    text='1',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "block_init" ---

# --- Initialize components for Routine "trial_init" ---

# --- Initialize components for Routine "LDTfix500" ---
LDTfix = visual.ShapeStim(
    win=win, name='LDTfix', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=0.025,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=0.0, interpolate=True)

# --- Initialize components for Routine "LDT" ---
LDTWord = visual.TextStim(win=win, name='LDTWord',
    text='',
    font='Arial',
    pos=[0,0], height=0.075, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
LDTResp = keyboard.Keyboard()

# --- Initialize components for Routine "blank500" ---
blank = visual.Rect(
    win=win, name='blank',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)
blankQResp = keyboard.Keyboard()

# --- Initialize components for Routine "PMCheck" ---

# --- Initialize components for Routine "block_break" ---
break_screen = visual.TextStim(win=win, name='break_screen',
    text='Break!\n\nThe next segment will begin in 5 seconds.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=1.2, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "LDTcountdown" ---
countdown5Text = visual.TextStim(win=win, name='countdown5Text',
    text='5',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
countdown4text = visual.TextStim(win=win, name='countdown4text',
    text='4',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
countdown3Text = visual.TextStim(win=win, name='countdown3Text',
    text='3',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
countdown2Text = visual.TextStim(win=win, name='countdown2Text',
    text='2',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
countdown1Text = visual.TextStim(win=win, name='countdown1Text',
    text='1',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# --- Initialize components for Routine "postExpInst" ---
postInstText = visual.TextStim(win=win, name='postInstText',
    text='Good job! Now, we would like you to answer a few questions about your experience during the task.\n\nPress ENTER to continue.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=1.2, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
postInstKey = keyboard.Keyboard()

# --- Initialize components for Routine "postExpQ1" ---
Q1Text = visual.TextStim(win=win, name='Q1Text',
    text='Do you remember being asked to press a specific button when you saw a type of word on the screen?\n\nIf yes, press "y".\nIf no, press "n"',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=1.2, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
Q1Key = keyboard.Keyboard()

# --- Initialize components for Routine "postExpQ2" ---
Q2Text = visual.TextStim(win=win, name='Q2Text',
    text='What was the type of word you were supposed to look for? Please type your answer below.',
    font='Arial',
    pos=(0, 0.15), height=0.05, wrapWidth=1.2, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Q2Textbox = visual.TextBox2(
     win, text=None, font='Arial',
     pos=(0, 0),     letterHeight=0.05,
     size=(0.5, 0.1), borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor='black',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='Q2Textbox',
     autoLog=True,
)
Q2Next = visual.TextStim(win=win, name='Q2Next',
    text='Press ENTER to submit your response.',
    font='Arial',
    pos=(0, -0.15), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
Q2Key = keyboard.Keyboard()

# --- Initialize components for Routine "postExpQ3" ---
Q3Text = visual.TextStim(win=win, name='Q3Text',
    text='What was the button you were supposed to press when you saw that word type? Please type your answer below.',
    font='Arial',
    pos=(0, 0.15), height=0.05, wrapWidth=1.2, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Q3Textbox = visual.TextBox2(
     win, text=None, font='Arial',
     pos=(0, 0),     letterHeight=0.05,
     size=(0.5, 0.1), borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor='black',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='Q3Textbox',
     autoLog=True,
)
Q3Next = visual.TextStim(win=win, name='Q3Next',
    text='Press SPACE to submit your response.',
    font='Arial',
    pos=(0, -0.15), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
Q3Key = keyboard.Keyboard()

# --- Initialize components for Routine "postExpQ4" ---
Q4Text = visual.TextStim(win=win, name='Q4Text',
    text='An animal word appeared in 20 of the segments.  How many times do you think you pressed "Q" in response to the an animal word? Please select a response from the options below.\n\n0. Never\n1. 1-5 times\n2. 6-10 times\n3. 11-15 times\n4. 16-20 times',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=1.2, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
Q4Key = keyboard.Keyboard()

# --- Initialize components for Routine "posExpQ5" ---
Q5Text = visual.TextStim(win=win, name='Q5Text',
    text='If you think you did not press "Q" in response to an animal word very often, why do you think that is? Please select an option from below.\n\n1. I did not see any animal words\n2. I forgot the word type I was supposed to look for\n3. I forgot the key I was supposed to press\n4. I responded to the animal words often',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=1.2, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
Q5Key = keyboard.Keyboard()

# --- Initialize components for Routine "postExpQ6" ---
Q6Text = visual.TextStim(win=win, name='Q6Text',
    text='Did you notice that the animal words appeared more often when the strings of letters were presented in a certain location?\n\nIf yes, press "y".\nIf no, press "n".',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Q6Key = keyboard.Keyboard()

# --- Initialize components for Routine "postExpQ7" ---
Q7Text = visual.TextStim(win=win, name='Q7Text',
    text='Did the animal words appear more often the upper or lower location on the screen?\n\nPress "u" for upper.\nPress "l" for lower.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
Q7Key = keyboard.Keyboard()

# --- Initialize components for Routine "postExpQ8" ---
Q8Text = visual.TextStim(win=win, name='Q8Text',
    text='Did you have any questions about the task or task instructions that you wish you could have asked the experimenter? If yes, please explain below. If no, leave blank.',
    font='Arial',
    pos=(0, 0.18), height=0.05, wrapWidth=1.2, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Q8Textbox = visual.TextBox2(
     win, text=None, font='Arial',
     pos=(0, 0),     letterHeight=0.05,
     size=(0.5, 0.1), borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor='black',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='Q8Textbox',
     autoLog=True,
)
Q8Next = visual.TextStim(win=win, name='Q8Next',
    text='Press SPACE to continue.',
    font='Arial',
    pos=(0, -0.175), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
Q8Key = keyboard.Keyboard()

# --- Initialize components for Routine "demoInst" ---
formInstText = visual.TextStim(win=win, name='formInstText',
    text='Before concluding the experiment, we would like you to answer a few questions about yourself.\n\n\nPress SPACE to begin the questions.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=1.2, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
formInstKey = keyboard.Keyboard()

# --- Initialize components for Routine "demoEducation" ---
eduText = visual.TextStim(win=win, name='eduText',
    text="Select the option that best describes your formal education level.\n\n1. Less than a high school degree\n2. High school degree\n3. Some college\n4. Bachelor's degree\n5. Master's degree\n6. Doctoral degree\n7. Prefer not to say",
    font='black',
    pos=(0, 0), height=0.05, wrapWidth=1.2, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
education = keyboard.Keyboard()

# --- Initialize components for Routine "demoMedication" ---
medText = visual.TextStim(win=win, name='medText',
    text='How many prescription drugs are you currently taking that may affect your memory? Please type your answer. If none, type 0. If you prefer not to answer, leave blank',
    font='Arial',
    pos=(0, 0.175), height=0.05, wrapWidth=1.2, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
medTextbox = visual.TextBox2(
     win, text=None, font='Arial',
     pos=(0, 0),     letterHeight=0.05,
     size=(0.5, 0.1), borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor='black',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='medTextbox',
     autoLog=True,
)
medNextText = visual.TextStim(win=win, name='medNextText',
    text='Press ENTER to submit your response.',
    font='Arial',
    pos=(0, -0.15), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
medNextKey = keyboard.Keyboard()

# --- Initialize components for Routine "demoHealth" ---
healthText = visual.TextStim(win=win, name='healthText',
    text='How would you rate your health at the moment?\n\n1. Poor\n2. Fair\n3. O.K.\n4. Good\n5. Excellent\n6. Prefer not to say',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=1.2, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
health = keyboard.Keyboard()

# --- Initialize components for Routine "demoHealthLimit" ---
healthLimitText = visual.TextStim(win=win, name='healthLimitText',
    text='How much do health problems limit your daily activities? \n\n1. A lot\n2. Some\n3. A little\n4. None\n5. Prefer not to say',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=1.2, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
healthLimit = keyboard.Keyboard()

# --- Initialize components for Routine "demoPsych" ---
psychText = visual.TextStim(win=win, name='psychText',
    text='Have you been diagnosed with one of the following neurological or psychiatric disorders?\n\n1. ADHD\n2. Bipolar Disorder\n3. Depression\n4. Anxiety\n5. Other\n6. More than one\n7. I have not been diagnosed with a neurological or psychiatric disorder',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=1.2, ori=0.0, 
    color='Black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
psychKey = keyboard.Keyboard()

# --- Initialize components for Routine "finish" ---
finishText = visual.TextStim(win=win, name='finishText',
    text="You're now done with the experiment. Please get the experimenter for further instructions.\n\nThank you for your participation!",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "init" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
initComponents = []
for thisComponent in initComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "init" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in initComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "init" ---
for thisComponent in initComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "init" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "welcome" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
welcomeKey.keys = []
welcomeKey.rt = []
_welcomeKey_allKeys = []
# keep track of which components have finished
welcomeComponents = [welcomeText, welcomeKey]
for thisComponent in welcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "welcome" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *welcomeText* updates
    if welcomeText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcomeText.frameNStart = frameN  # exact frame index
        welcomeText.tStart = t  # local t and not account for scr refresh
        welcomeText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcomeText, 'tStartRefresh')  # time at next scr refresh
        welcomeText.setAutoDraw(True)
    
    # *welcomeKey* updates
    waitOnFlip = False
    if welcomeKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcomeKey.frameNStart = frameN  # exact frame index
        welcomeKey.tStart = t  # local t and not account for scr refresh
        welcomeKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcomeKey, 'tStartRefresh')  # time at next scr refresh
        welcomeKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(welcomeKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(welcomeKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if welcomeKey.status == STARTED and not waitOnFlip:
        theseKeys = welcomeKey.getKeys(keyList=['return'], waitRelease=False)
        _welcomeKey_allKeys.extend(theseKeys)
        if len(_welcomeKey_allKeys):
            welcomeKey.keys = _welcomeKey_allKeys[-1].name  # just the last key pressed
            welcomeKey.rt = _welcomeKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "welcome" ---
for thisComponent in welcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "demo1Inst" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
demoInstTextKey.keys = []
demoInstTextKey.rt = []
_demoInstTextKey_allKeys = []
# keep track of which components have finished
demo1InstComponents = [demo1InstText, demoInstTextKey]
for thisComponent in demo1InstComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "demo1Inst" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *demo1InstText* updates
    if demo1InstText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demo1InstText.frameNStart = frameN  # exact frame index
        demo1InstText.tStart = t  # local t and not account for scr refresh
        demo1InstText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demo1InstText, 'tStartRefresh')  # time at next scr refresh
        demo1InstText.setAutoDraw(True)
    
    # *demoInstTextKey* updates
    waitOnFlip = False
    if demoInstTextKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demoInstTextKey.frameNStart = frameN  # exact frame index
        demoInstTextKey.tStart = t  # local t and not account for scr refresh
        demoInstTextKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demoInstTextKey, 'tStartRefresh')  # time at next scr refresh
        demoInstTextKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(demoInstTextKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(demoInstTextKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if demoInstTextKey.status == STARTED and not waitOnFlip:
        theseKeys = demoInstTextKey.getKeys(keyList=['return'], waitRelease=False)
        _demoInstTextKey_allKeys.extend(theseKeys)
        if len(_demoInstTextKey_allKeys):
            demoInstTextKey.keys = _demoInstTextKey_allKeys[-1].name  # just the last key pressed
            demoInstTextKey.rt = _demoInstTextKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in demo1InstComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "demo1Inst" ---
for thisComponent in demo1InstComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "demo1Inst" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "demoAge" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
ageTextbox.reset()
ageNextKey.keys = []
ageNextKey.rt = []
_ageNextKey_allKeys = []
# keep track of which components have finished
demoAgeComponents = [ageText, ageTextbox, ageNextText, ageNextKey]
for thisComponent in demoAgeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "demoAge" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ageText* updates
    if ageText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ageText.frameNStart = frameN  # exact frame index
        ageText.tStart = t  # local t and not account for scr refresh
        ageText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ageText, 'tStartRefresh')  # time at next scr refresh
        ageText.setAutoDraw(True)
    
    # *ageTextbox* updates
    if ageTextbox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ageTextbox.frameNStart = frameN  # exact frame index
        ageTextbox.tStart = t  # local t and not account for scr refresh
        ageTextbox.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ageTextbox, 'tStartRefresh')  # time at next scr refresh
        ageTextbox.setAutoDraw(True)
    
    # *ageNextText* updates
    if ageNextText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ageNextText.frameNStart = frameN  # exact frame index
        ageNextText.tStart = t  # local t and not account for scr refresh
        ageNextText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ageNextText, 'tStartRefresh')  # time at next scr refresh
        ageNextText.setAutoDraw(True)
    
    # *ageNextKey* updates
    waitOnFlip = False
    if ageNextKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ageNextKey.frameNStart = frameN  # exact frame index
        ageNextKey.tStart = t  # local t and not account for scr refresh
        ageNextKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ageNextKey, 'tStartRefresh')  # time at next scr refresh
        ageNextKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(ageNextKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(ageNextKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if ageNextKey.status == STARTED and not waitOnFlip:
        theseKeys = ageNextKey.getKeys(keyList=['space'], waitRelease=False)
        _ageNextKey_allKeys.extend(theseKeys)
        if len(_ageNextKey_allKeys):
            ageNextKey.keys = _ageNextKey_allKeys[-1].name  # just the last key pressed
            ageNextKey.rt = _ageNextKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in demoAgeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "demoAge" ---
for thisComponent in demoAgeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ageTextbox.text',ageTextbox.text)
# the Routine "demoAge" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "demoGender" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
genderTextbox.reset()
genderNextKey.keys = []
genderNextKey.rt = []
_genderNextKey_allKeys = []
# keep track of which components have finished
demoGenderComponents = [genderText, genderTextbox, genderNextText, genderNextKey]
for thisComponent in demoGenderComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "demoGender" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *genderText* updates
    if genderText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        genderText.frameNStart = frameN  # exact frame index
        genderText.tStart = t  # local t and not account for scr refresh
        genderText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(genderText, 'tStartRefresh')  # time at next scr refresh
        genderText.setAutoDraw(True)
    
    # *genderTextbox* updates
    if genderTextbox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        genderTextbox.frameNStart = frameN  # exact frame index
        genderTextbox.tStart = t  # local t and not account for scr refresh
        genderTextbox.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(genderTextbox, 'tStartRefresh')  # time at next scr refresh
        genderTextbox.setAutoDraw(True)
    
    # *genderNextText* updates
    if genderNextText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        genderNextText.frameNStart = frameN  # exact frame index
        genderNextText.tStart = t  # local t and not account for scr refresh
        genderNextText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(genderNextText, 'tStartRefresh')  # time at next scr refresh
        genderNextText.setAutoDraw(True)
    
    # *genderNextKey* updates
    waitOnFlip = False
    if genderNextKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        genderNextKey.frameNStart = frameN  # exact frame index
        genderNextKey.tStart = t  # local t and not account for scr refresh
        genderNextKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(genderNextKey, 'tStartRefresh')  # time at next scr refresh
        genderNextKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(genderNextKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(genderNextKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if genderNextKey.status == STARTED and not waitOnFlip:
        theseKeys = genderNextKey.getKeys(keyList=['return'], waitRelease=False)
        _genderNextKey_allKeys.extend(theseKeys)
        if len(_genderNextKey_allKeys):
            genderNextKey.keys = _genderNextKey_allKeys[-1].name  # just the last key pressed
            genderNextKey.rt = _genderNextKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in demoGenderComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "demoGender" ---
for thisComponent in demoGenderComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('genderTextbox.text',genderTextbox.text)
# the Routine "demoGender" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
demoRace_loop = data.TrialHandler(nReps=5.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='demoRace_loop')
thisExp.addLoop(demoRace_loop)  # add the loop to the experiment
thisDemoRace_loop = demoRace_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisDemoRace_loop.rgb)
if thisDemoRace_loop != None:
    for paramName in thisDemoRace_loop:
        exec('{} = thisDemoRace_loop[paramName]'.format(paramName))

for thisDemoRace_loop in demoRace_loop:
    currentLoop = demoRace_loop
    # abbreviate parameter names if possible (e.g. rgb = thisDemoRace_loop.rgb)
    if thisDemoRace_loop != None:
        for paramName in thisDemoRace_loop:
            exec('{} = thisDemoRace_loop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "demoRace_init" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from raceCode
    raceList = ['American Indian or Alaska Native', 'Asian','Black or African American','Native Hawaiian or other Pacific Islander','White']
    
    race = 'Are you ' + str(raceList[demoRace_loop.thisN]) + '?'
    # keep track of which components have finished
    demoRace_initComponents = []
    for thisComponent in demoRace_initComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "demoRace_init" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in demoRace_initComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "demoRace_init" ---
    for thisComponent in demoRace_initComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "demoRace_init" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "demoRace" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    raceText.setText(race)
    raceResp.keys = []
    raceResp.rt = []
    _raceResp_allKeys = []
    # keep track of which components have finished
    demoRaceComponents = [raceText, raceOpts, raceResp]
    for thisComponent in demoRaceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "demoRace" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *raceText* updates
        if raceText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            raceText.frameNStart = frameN  # exact frame index
            raceText.tStart = t  # local t and not account for scr refresh
            raceText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(raceText, 'tStartRefresh')  # time at next scr refresh
            raceText.setAutoDraw(True)
        
        # *raceOpts* updates
        if raceOpts.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            raceOpts.frameNStart = frameN  # exact frame index
            raceOpts.tStart = t  # local t and not account for scr refresh
            raceOpts.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(raceOpts, 'tStartRefresh')  # time at next scr refresh
            raceOpts.setAutoDraw(True)
        
        # *raceResp* updates
        waitOnFlip = False
        if raceResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            raceResp.frameNStart = frameN  # exact frame index
            raceResp.tStart = t  # local t and not account for scr refresh
            raceResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(raceResp, 'tStartRefresh')  # time at next scr refresh
            raceResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(raceResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(raceResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if raceResp.status == STARTED and not waitOnFlip:
            theseKeys = raceResp.getKeys(keyList=['y','n','x'], waitRelease=False)
            _raceResp_allKeys.extend(theseKeys)
            if len(_raceResp_allKeys):
                raceResp.keys = _raceResp_allKeys[-1].name  # just the last key pressed
                raceResp.rt = _raceResp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in demoRaceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "demoRace" ---
    for thisComponent in demoRaceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from storeResp
    thisExp.addData('race',raceList[demoRace_loop.thisN])
    thisExp.addData('raceResp', raceResp.keys)
    # Run 'End Routine' code from raceEnd
    event.clearEvents('keyboard')
    # the Routine "demoRace" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 5.0 repeats of 'demoRace_loop'


# set up handler to look after randomisation of conditions etc
LDTunderstand = data.TrialHandler(nReps=2.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='LDTunderstand')
thisExp.addLoop(LDTunderstand)  # add the loop to the experiment
thisLDTunderstand = LDTunderstand.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLDTunderstand.rgb)
if thisLDTunderstand != None:
    for paramName in thisLDTunderstand:
        exec('{} = thisLDTunderstand[paramName]'.format(paramName))

for thisLDTunderstand in LDTunderstand:
    currentLoop = LDTunderstand
    # abbreviate parameter names if possible (e.g. rgb = thisLDTunderstand.rgb)
    if thisLDTunderstand != None:
        for paramName in thisLDTunderstand:
            exec('{} = thisLDTunderstand[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "LDTreread" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from LDTrereadCode
    if LDTunderstand.thisN == 0:
        continueRoutine = False
    LDTrereadKey.keys = []
    LDTrereadKey.rt = []
    _LDTrereadKey_allKeys = []
    # keep track of which components have finished
    LDTrereadComponents = [LDTrereadText, LDTrereadKey]
    for thisComponent in LDTrereadComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "LDTreread" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *LDTrereadText* updates
        if LDTrereadText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            LDTrereadText.frameNStart = frameN  # exact frame index
            LDTrereadText.tStart = t  # local t and not account for scr refresh
            LDTrereadText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(LDTrereadText, 'tStartRefresh')  # time at next scr refresh
            LDTrereadText.setAutoDraw(True)
        
        # *LDTrereadKey* updates
        waitOnFlip = False
        if LDTrereadKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            LDTrereadKey.frameNStart = frameN  # exact frame index
            LDTrereadKey.tStart = t  # local t and not account for scr refresh
            LDTrereadKey.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(LDTrereadKey, 'tStartRefresh')  # time at next scr refresh
            LDTrereadKey.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(LDTrereadKey.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(LDTrereadKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if LDTrereadKey.status == STARTED and not waitOnFlip:
            theseKeys = LDTrereadKey.getKeys(keyList=['return'], waitRelease=False)
            _LDTrereadKey_allKeys.extend(theseKeys)
            if len(_LDTrereadKey_allKeys):
                LDTrereadKey.keys = _LDTrereadKey_allKeys[-1].name  # just the last key pressed
                LDTrereadKey.rt = _LDTrereadKey_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in LDTrereadComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "LDTreread" ---
    for thisComponent in LDTrereadComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "LDTreread" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "LDTInst1" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    LDTInst1Key.keys = []
    LDTInst1Key.rt = []
    _LDTInst1Key_allKeys = []
    # keep track of which components have finished
    LDTInst1Components = [LDTInst1Text, LDTInst1Key]
    for thisComponent in LDTInst1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "LDTInst1" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *LDTInst1Text* updates
        if LDTInst1Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            LDTInst1Text.frameNStart = frameN  # exact frame index
            LDTInst1Text.tStart = t  # local t and not account for scr refresh
            LDTInst1Text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(LDTInst1Text, 'tStartRefresh')  # time at next scr refresh
            LDTInst1Text.setAutoDraw(True)
        
        # *LDTInst1Key* updates
        waitOnFlip = False
        if LDTInst1Key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            LDTInst1Key.frameNStart = frameN  # exact frame index
            LDTInst1Key.tStart = t  # local t and not account for scr refresh
            LDTInst1Key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(LDTInst1Key, 'tStartRefresh')  # time at next scr refresh
            LDTInst1Key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(LDTInst1Key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(LDTInst1Key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if LDTInst1Key.status == STARTED and not waitOnFlip:
            theseKeys = LDTInst1Key.getKeys(keyList=['g'], waitRelease=False)
            _LDTInst1Key_allKeys.extend(theseKeys)
            if len(_LDTInst1Key_allKeys):
                LDTInst1Key.keys = _LDTInst1Key_allKeys[-1].name  # just the last key pressed
                LDTInst1Key.rt = _LDTInst1Key_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in LDTInst1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "LDTInst1" ---
    for thisComponent in LDTInst1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "LDTInst1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "LDTInst2" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    LDTInst2Key.keys = []
    LDTInst2Key.rt = []
    _LDTInst2Key_allKeys = []
    # keep track of which components have finished
    LDTInst2Components = [LDTInst2Text, LDTInst2Key]
    for thisComponent in LDTInst2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "LDTInst2" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *LDTInst2Text* updates
        if LDTInst2Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            LDTInst2Text.frameNStart = frameN  # exact frame index
            LDTInst2Text.tStart = t  # local t and not account for scr refresh
            LDTInst2Text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(LDTInst2Text, 'tStartRefresh')  # time at next scr refresh
            LDTInst2Text.setAutoDraw(True)
        
        # *LDTInst2Key* updates
        waitOnFlip = False
        if LDTInst2Key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            LDTInst2Key.frameNStart = frameN  # exact frame index
            LDTInst2Key.tStart = t  # local t and not account for scr refresh
            LDTInst2Key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(LDTInst2Key, 'tStartRefresh')  # time at next scr refresh
            LDTInst2Key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(LDTInst2Key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(LDTInst2Key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if LDTInst2Key.status == STARTED and not waitOnFlip:
            theseKeys = LDTInst2Key.getKeys(keyList=['return'], waitRelease=False)
            _LDTInst2Key_allKeys.extend(theseKeys)
            if len(_LDTInst2Key_allKeys):
                LDTInst2Key.keys = _LDTInst2Key_allKeys[-1].name  # just the last key pressed
                LDTInst2Key.rt = _LDTInst2Key_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in LDTInst2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "LDTInst2" ---
    for thisComponent in LDTInst2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "LDTInst2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "LDTInst3" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    LDTInst3Key.keys = []
    LDTInst3Key.rt = []
    _LDTInst3Key_allKeys = []
    # keep track of which components have finished
    LDTInst3Components = [LDTInst3Text, LDTInst3Key]
    for thisComponent in LDTInst3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "LDTInst3" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *LDTInst3Text* updates
        if LDTInst3Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            LDTInst3Text.frameNStart = frameN  # exact frame index
            LDTInst3Text.tStart = t  # local t and not account for scr refresh
            LDTInst3Text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(LDTInst3Text, 'tStartRefresh')  # time at next scr refresh
            LDTInst3Text.setAutoDraw(True)
        
        # *LDTInst3Key* updates
        waitOnFlip = False
        if LDTInst3Key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            LDTInst3Key.frameNStart = frameN  # exact frame index
            LDTInst3Key.tStart = t  # local t and not account for scr refresh
            LDTInst3Key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(LDTInst3Key, 'tStartRefresh')  # time at next scr refresh
            LDTInst3Key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(LDTInst3Key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(LDTInst3Key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if LDTInst3Key.status == STARTED and not waitOnFlip:
            theseKeys = LDTInst3Key.getKeys(keyList=['space'], waitRelease=False)
            _LDTInst3Key_allKeys.extend(theseKeys)
            if len(_LDTInst3Key_allKeys):
                LDTInst3Key.keys = _LDTInst3Key_allKeys[-1].name  # just the last key pressed
                LDTInst3Key.rt = _LDTInst3Key_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in LDTInst3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "LDTInst3" ---
    for thisComponent in LDTInst3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "LDTInst3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "LDTcheck" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    LDTcheckKey.keys = []
    LDTcheckKey.rt = []
    _LDTcheckKey_allKeys = []
    # keep track of which components have finished
    LDTcheckComponents = [LDTcheckText, LDTcheckKey]
    for thisComponent in LDTcheckComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "LDTcheck" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *LDTcheckText* updates
        if LDTcheckText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            LDTcheckText.frameNStart = frameN  # exact frame index
            LDTcheckText.tStart = t  # local t and not account for scr refresh
            LDTcheckText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(LDTcheckText, 'tStartRefresh')  # time at next scr refresh
            LDTcheckText.setAutoDraw(True)
        
        # *LDTcheckKey* updates
        waitOnFlip = False
        if LDTcheckKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            LDTcheckKey.frameNStart = frameN  # exact frame index
            LDTcheckKey.tStart = t  # local t and not account for scr refresh
            LDTcheckKey.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(LDTcheckKey, 'tStartRefresh')  # time at next scr refresh
            LDTcheckKey.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(LDTcheckKey.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(LDTcheckKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if LDTcheckKey.status == STARTED and not waitOnFlip:
            theseKeys = LDTcheckKey.getKeys(keyList=['y','n'], waitRelease=False)
            _LDTcheckKey_allKeys.extend(theseKeys)
            if len(_LDTcheckKey_allKeys):
                LDTcheckKey.keys = _LDTcheckKey_allKeys[-1].name  # just the last key pressed
                LDTcheckKey.rt = _LDTcheckKey_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in LDTcheckComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "LDTcheck" ---
    for thisComponent in LDTcheckComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from LDTunderCode
    thisExp.addData("LDTunderstand", LDTcheckKey.keys)
    if LDTcheckKey.keys == 'y':
        LDTunderstand.finished = True
    elif LDTcheckKey.keys == 'Y':
        LDTunderstand.finished = True
    # the Routine "LDTcheck" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'LDTunderstand'


# --- Prepare to start Routine "LDTInst5" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
LDTInst5Key.keys = []
LDTInst5Key.rt = []
_LDTInst5Key_allKeys = []
# keep track of which components have finished
LDTInst5Components = [LDTInst5Text, LDTInst5Key]
for thisComponent in LDTInst5Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "LDTInst5" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *LDTInst5Text* updates
    if LDTInst5Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        LDTInst5Text.frameNStart = frameN  # exact frame index
        LDTInst5Text.tStart = t  # local t and not account for scr refresh
        LDTInst5Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(LDTInst5Text, 'tStartRefresh')  # time at next scr refresh
        LDTInst5Text.setAutoDraw(True)
    
    # *LDTInst5Key* updates
    waitOnFlip = False
    if LDTInst5Key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        LDTInst5Key.frameNStart = frameN  # exact frame index
        LDTInst5Key.tStart = t  # local t and not account for scr refresh
        LDTInst5Key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(LDTInst5Key, 'tStartRefresh')  # time at next scr refresh
        LDTInst5Key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(LDTInst5Key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(LDTInst5Key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if LDTInst5Key.status == STARTED and not waitOnFlip:
        theseKeys = LDTInst5Key.getKeys(keyList=['return'], waitRelease=False)
        _LDTInst5Key_allKeys.extend(theseKeys)
        if len(_LDTInst5Key_allKeys):
            LDTInst5Key.keys = _LDTInst5Key_allKeys[-1].name  # just the last key pressed
            LDTInst5Key.rt = _LDTInst5Key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in LDTInst5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "LDTInst5" ---
for thisComponent in LDTInst5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "LDTInst5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "countdown" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
countdownComponents = [five, four, three, two, one]
for thisComponent in countdownComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "countdown" ---
while continueRoutine and routineTimer.getTime() < 5.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *five* updates
    if five.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        five.frameNStart = frameN  # exact frame index
        five.tStart = t  # local t and not account for scr refresh
        five.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(five, 'tStartRefresh')  # time at next scr refresh
        five.setAutoDraw(True)
    if five.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > five.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            five.tStop = t  # not accounting for scr refresh
            five.frameNStop = frameN  # exact frame index
            five.setAutoDraw(False)
    
    # *four* updates
    if four.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        four.frameNStart = frameN  # exact frame index
        four.tStart = t  # local t and not account for scr refresh
        four.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(four, 'tStartRefresh')  # time at next scr refresh
        four.setAutoDraw(True)
    if four.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > four.tStartRefresh + 1-frameTolerance:
            # keep track of stop time/frame for later
            four.tStop = t  # not accounting for scr refresh
            four.frameNStop = frameN  # exact frame index
            four.setAutoDraw(False)
    
    # *three* updates
    if three.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        three.frameNStart = frameN  # exact frame index
        three.tStart = t  # local t and not account for scr refresh
        three.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(three, 'tStartRefresh')  # time at next scr refresh
        three.setAutoDraw(True)
    if three.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > three.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            three.tStop = t  # not accounting for scr refresh
            three.frameNStop = frameN  # exact frame index
            three.setAutoDraw(False)
    
    # *two* updates
    if two.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
        # keep track of start time/frame for later
        two.frameNStart = frameN  # exact frame index
        two.tStart = t  # local t and not account for scr refresh
        two.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(two, 'tStartRefresh')  # time at next scr refresh
        two.setAutoDraw(True)
    if two.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > two.tStartRefresh + 1-frameTolerance:
            # keep track of stop time/frame for later
            two.tStop = t  # not accounting for scr refresh
            two.frameNStop = frameN  # exact frame index
            two.setAutoDraw(False)
    
    # *one* updates
    if one.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
        # keep track of start time/frame for later
        one.frameNStart = frameN  # exact frame index
        one.tStart = t  # local t and not account for scr refresh
        one.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(one, 'tStartRefresh')  # time at next scr refresh
        one.setAutoDraw(True)
    if one.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > one.tStartRefresh + 1-frameTolerance:
            # keep track of stop time/frame for later
            one.tStop = t  # not accounting for scr refresh
            one.frameNStop = frameN  # exact frame index
            one.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in countdownComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "countdown" ---
for thisComponent in countdownComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-5.000000)

# set up handler to look after randomisation of conditions etc
pracBlocks = data.TrialHandler(nReps=0.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='pracBlocks')
thisExp.addLoop(pracBlocks)  # add the loop to the experiment
thisPracBlock = pracBlocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPracBlock.rgb)
if thisPracBlock != None:
    for paramName in thisPracBlock:
        exec('{} = thisPracBlock[paramName]'.format(paramName))

for thisPracBlock in pracBlocks:
    currentLoop = pracBlocks
    # abbreviate parameter names if possible (e.g. rgb = thisPracBlock.rgb)
    if thisPracBlock != None:
        for paramName in thisPracBlock:
            exec('{} = thisPracBlock[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "pracBlockinit" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from pracBlockCode
    nCorr = 0
    
    if subNum %4 == 0:
        pracSL = [['upper']*int(nPracTrials)] + [['lower']*int(nPracTrials)]
    elif subNum %4 == 1:
        pracSL = [['lower']*int(nPracTrials)] + [['upper']*int(nPracTrials)]
    elif subNum %4 == 2:
        pracSL = [['upper']*int(nPracTrials)] + [['lower']*int(nPracTrials)]
    elif subNum %4 == 3:
        pracSL = [['lower']*int(nPracTrials)] + [['upper']*int(nPracTrials)]
    
    this_pracS = pracStim[pracBlocks.thisN]
    this_pracWT = pracWordType[pracBlocks.thisN]
    this_pracCK = pracCorrKey[pracBlocks.thisN]
    this_pracStimLoc = pracSL[pracBlocks.thisN]
    # keep track of which components have finished
    pracBlockinitComponents = []
    for thisComponent in pracBlockinitComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "pracBlockinit" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pracBlockinitComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "pracBlockinit" ---
    for thisComponent in pracBlockinitComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "pracBlockinit" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    pracTrial = data.TrialHandler(nReps=nPracTrials, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='pracTrial')
    thisExp.addLoop(pracTrial)  # add the loop to the experiment
    thisPracTrial = pracTrial.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPracTrial.rgb)
    if thisPracTrial != None:
        for paramName in thisPracTrial:
            exec('{} = thisPracTrial[paramName]'.format(paramName))
    
    for thisPracTrial in pracTrial:
        currentLoop = pracTrial
        # abbreviate parameter names if possible (e.g. rgb = thisPracTrial.rgb)
        if thisPracTrial != None:
            for paramName in thisPracTrial:
                exec('{} = thisPracTrial[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "pracTrialinit" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from pracTrialCode
        pStim = this_pracS[pracTrial.thisN]
        pWordType = this_pracWT[pracTrial.thisN]
        pCorrKey = this_pracCK[pracTrial.thisN]
        pLoc = this_pracStimLoc[pracTrial.thisN]
        if pLoc == 'upper':
            pStimLoc = [0,0.25]
        else:
            pStimLoc = [0,-0.25]
        
        thisExp.addData('stim', pStim)
        thisExp.addData('word_type', pWordType)
        thisExp.addData('corr_key', pCorrKey)
        thisExp.addData('stim_location', pLoc)
        # keep track of which components have finished
        pracTrialinitComponents = []
        for thisComponent in pracTrialinitComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "pracTrialinit" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in pracTrialinitComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "pracTrialinit" ---
        for thisComponent in pracTrialinitComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "pracTrialinit" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "pracfix500" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        fixcross.setPos(pStimLoc)
        # keep track of which components have finished
        pracfix500Components = [fixcross]
        for thisComponent in pracfix500Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "pracfix500" ---
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixcross* updates
            if fixcross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixcross.frameNStart = frameN  # exact frame index
                fixcross.tStart = t  # local t and not account for scr refresh
                fixcross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixcross, 'tStartRefresh')  # time at next scr refresh
                fixcross.setAutoDraw(True)
            if fixcross.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixcross.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fixcross.tStop = t  # not accounting for scr refresh
                    fixcross.frameNStop = frameN  # exact frame index
                    fixcross.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in pracfix500Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "pracfix500" ---
        for thisComponent in pracfix500Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        
        # --- Prepare to start Routine "LDTprac" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        LDTpracWord.setPos(pStimLoc)
        LDTpracWord.setText(pStim)
        LDTpracKey.keys = []
        LDTpracKey.rt = []
        _LDTpracKey_allKeys = []
        # keep track of which components have finished
        LDTpracComponents = [LDTpracWord, LDTpracKey]
        for thisComponent in LDTpracComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "LDTprac" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *LDTpracWord* updates
            if LDTpracWord.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                LDTpracWord.frameNStart = frameN  # exact frame index
                LDTpracWord.tStart = t  # local t and not account for scr refresh
                LDTpracWord.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(LDTpracWord, 'tStartRefresh')  # time at next scr refresh
                LDTpracWord.setAutoDraw(True)
            
            # *LDTpracKey* updates
            waitOnFlip = False
            if LDTpracKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                LDTpracKey.frameNStart = frameN  # exact frame index
                LDTpracKey.tStart = t  # local t and not account for scr refresh
                LDTpracKey.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(LDTpracKey, 'tStartRefresh')  # time at next scr refresh
                LDTpracKey.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(LDTpracKey.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(LDTpracKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if LDTpracKey.status == STARTED and not waitOnFlip:
                theseKeys = LDTpracKey.getKeys(keyList=['g','h'], waitRelease=False)
                _LDTpracKey_allKeys.extend(theseKeys)
                if len(_LDTpracKey_allKeys):
                    LDTpracKey.keys = _LDTpracKey_allKeys[-1].name  # just the last key pressed
                    LDTpracKey.rt = _LDTpracKey_allKeys[-1].rt
                    # was this correct?
                    if (LDTpracKey.keys == str(pCorrKey)) or (LDTpracKey.keys == pCorrKey):
                        LDTpracKey.corr = 1
                    else:
                        LDTpracKey.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in LDTpracComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "LDTprac" ---
        for thisComponent in LDTpracComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if LDTpracKey.keys in ['', [], None]:  # No response was made
            LDTpracKey.keys = None
            # was no response the correct answer?!
            if str(pCorrKey).lower() == 'none':
               LDTpracKey.corr = 1;  # correct non-response
            else:
               LDTpracKey.corr = 0;  # failed to respond (incorrectly)
        # store data for pracTrial (TrialHandler)
        pracTrial.addData('LDTpracKey.keys',LDTpracKey.keys)
        pracTrial.addData('LDTpracKey.corr', LDTpracKey.corr)
        if LDTpracKey.keys != None:  # we had a response
            pracTrial.addData('LDTpracKey.rt', LDTpracKey.rt)
        # the Routine "LDTprac" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "pracFeedback" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from pracFeedbackCode
        nCorr += LDTpracKey.corr
        running_average = nCorr/(pracTrial.thisN + 1)
        
        if LDTpracKey.corr == 1:
            feedback = 'Correct!\n\n' + str(round(LDTpracKey.rt,2)) + ' Seconds Response Time\n\n' + str(round((running_average*100),1)) + '% Average Percent Correct'
            font_color = 'blue'
        else:
            feedback = 'Incorrect\n\n' + str(round(LDTpracKey.rt,2)) + ' Seconds Response Time\n\n' + str(round((running_average*100),1)) + '% Average Percent Correct'
            font_color = 'red'
        LDTpracFeedback.setColor(font_color, colorSpace='rgb')
        LDTpracFeedback.setText(feedback)
        # keep track of which components have finished
        pracFeedbackComponents = [LDTpracFeedback]
        for thisComponent in pracFeedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "pracFeedback" ---
        while continueRoutine and routineTimer.getTime() < 1.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *LDTpracFeedback* updates
            if LDTpracFeedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                LDTpracFeedback.frameNStart = frameN  # exact frame index
                LDTpracFeedback.tStart = t  # local t and not account for scr refresh
                LDTpracFeedback.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(LDTpracFeedback, 'tStartRefresh')  # time at next scr refresh
                LDTpracFeedback.setAutoDraw(True)
            if LDTpracFeedback.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > LDTpracFeedback.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    LDTpracFeedback.tStop = t  # not accounting for scr refresh
                    LDTpracFeedback.frameNStop = frameN  # exact frame index
                    LDTpracFeedback.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in pracFeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "pracFeedback" ---
        for thisComponent in pracFeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.500000)
        thisExp.nextEntry()
        
    # completed nPracTrials repeats of 'pracTrial'
    
    
    # --- Prepare to start Routine "pracBreak" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from pracBreakCode
    if (int(pracBlocks.thisN) + 1) == nPracBlock:
        continueRoutine = False
    else:
        continueRoutine = True
    # keep track of which components have finished
    pracBreakComponents = [pracBreakText]
    for thisComponent in pracBreakComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "pracBreak" ---
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *pracBreakText* updates
        if pracBreakText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pracBreakText.frameNStart = frameN  # exact frame index
            pracBreakText.tStart = t  # local t and not account for scr refresh
            pracBreakText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pracBreakText, 'tStartRefresh')  # time at next scr refresh
            pracBreakText.setAutoDraw(True)
        if pracBreakText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > pracBreakText.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                pracBreakText.tStop = t  # not accounting for scr refresh
                pracBreakText.frameNStop = frameN  # exact frame index
                pracBreakText.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pracBreakComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "pracBreak" ---
    for thisComponent in pracBreakComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    
    # --- Prepare to start Routine "pracCountdown" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from pracCountCode
    if (int(pracBlocks.thisN) + 1) == nPracBlock:
        continueRoutine = False
    else:
        continueRoutine = True
    # keep track of which components have finished
    pracCountdownComponents = [fiveText, fourText, threeText, twoText, oneText]
    for thisComponent in pracCountdownComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "pracCountdown" ---
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fiveText* updates
        if fiveText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fiveText.frameNStart = frameN  # exact frame index
            fiveText.tStart = t  # local t and not account for scr refresh
            fiveText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fiveText, 'tStartRefresh')  # time at next scr refresh
            fiveText.setAutoDraw(True)
        if fiveText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fiveText.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                fiveText.tStop = t  # not accounting for scr refresh
                fiveText.frameNStop = frameN  # exact frame index
                fiveText.setAutoDraw(False)
        
        # *fourText* updates
        if fourText.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            fourText.frameNStart = frameN  # exact frame index
            fourText.tStart = t  # local t and not account for scr refresh
            fourText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fourText, 'tStartRefresh')  # time at next scr refresh
            fourText.setAutoDraw(True)
        if fourText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fourText.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                fourText.tStop = t  # not accounting for scr refresh
                fourText.frameNStop = frameN  # exact frame index
                fourText.setAutoDraw(False)
        
        # *threeText* updates
        if threeText.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            threeText.frameNStart = frameN  # exact frame index
            threeText.tStart = t  # local t and not account for scr refresh
            threeText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(threeText, 'tStartRefresh')  # time at next scr refresh
            threeText.setAutoDraw(True)
        if threeText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > threeText.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                threeText.tStop = t  # not accounting for scr refresh
                threeText.frameNStop = frameN  # exact frame index
                threeText.setAutoDraw(False)
        
        # *twoText* updates
        if twoText.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            twoText.frameNStart = frameN  # exact frame index
            twoText.tStart = t  # local t and not account for scr refresh
            twoText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(twoText, 'tStartRefresh')  # time at next scr refresh
            twoText.setAutoDraw(True)
        if twoText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > twoText.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                twoText.tStop = t  # not accounting for scr refresh
                twoText.frameNStop = frameN  # exact frame index
                twoText.setAutoDraw(False)
        
        # *oneText* updates
        if oneText.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
            # keep track of start time/frame for later
            oneText.frameNStart = frameN  # exact frame index
            oneText.tStart = t  # local t and not account for scr refresh
            oneText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(oneText, 'tStartRefresh')  # time at next scr refresh
            oneText.setAutoDraw(True)
        if oneText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > oneText.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                oneText.tStop = t  # not accounting for scr refresh
                oneText.frameNStop = frameN  # exact frame index
                oneText.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pracCountdownComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "pracCountdown" ---
    for thisComponent in pracCountdownComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    thisExp.nextEntry()
    
# completed 0.0 repeats of 'pracBlocks'


# set up handler to look after randomisation of conditions etc
PMunderstand = data.TrialHandler(nReps=2.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='PMunderstand')
thisExp.addLoop(PMunderstand)  # add the loop to the experiment
thisPMunderstand = PMunderstand.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPMunderstand.rgb)
if thisPMunderstand != None:
    for paramName in thisPMunderstand:
        exec('{} = thisPMunderstand[paramName]'.format(paramName))

for thisPMunderstand in PMunderstand:
    currentLoop = PMunderstand
    # abbreviate parameter names if possible (e.g. rgb = thisPMunderstand.rgb)
    if thisPMunderstand != None:
        for paramName in thisPMunderstand:
            exec('{} = thisPMunderstand[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "PMreread" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from PMrereadCode
    if PMunderstand.thisN == 0:
        continueRoutine = False
    PMrereadKey.keys = []
    PMrereadKey.rt = []
    _PMrereadKey_allKeys = []
    # keep track of which components have finished
    PMrereadComponents = [PMrereadtext, PMrereadKey]
    for thisComponent in PMrereadComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "PMreread" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *PMrereadtext* updates
        if PMrereadtext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            PMrereadtext.frameNStart = frameN  # exact frame index
            PMrereadtext.tStart = t  # local t and not account for scr refresh
            PMrereadtext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PMrereadtext, 'tStartRefresh')  # time at next scr refresh
            PMrereadtext.setAutoDraw(True)
        
        # *PMrereadKey* updates
        waitOnFlip = False
        if PMrereadKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            PMrereadKey.frameNStart = frameN  # exact frame index
            PMrereadKey.tStart = t  # local t and not account for scr refresh
            PMrereadKey.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PMrereadKey, 'tStartRefresh')  # time at next scr refresh
            PMrereadKey.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(PMrereadKey.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(PMrereadKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if PMrereadKey.status == STARTED and not waitOnFlip:
            theseKeys = PMrereadKey.getKeys(keyList=['return'], waitRelease=False)
            _PMrereadKey_allKeys.extend(theseKeys)
            if len(_PMrereadKey_allKeys):
                PMrereadKey.keys = _PMrereadKey_allKeys[-1].name  # just the last key pressed
                PMrereadKey.rt = _PMrereadKey_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PMrereadComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "PMreread" ---
    for thisComponent in PMrereadComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "PMreread" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "PMinst1" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    PMinst1Key.keys = []
    PMinst1Key.rt = []
    _PMinst1Key_allKeys = []
    # keep track of which components have finished
    PMinst1Components = [PMinstBackground, pmInst1Text, PMinst1Key]
    for thisComponent in PMinst1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "PMinst1" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *PMinstBackground* updates
        if PMinstBackground.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            PMinstBackground.frameNStart = frameN  # exact frame index
            PMinstBackground.tStart = t  # local t and not account for scr refresh
            PMinstBackground.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PMinstBackground, 'tStartRefresh')  # time at next scr refresh
            PMinstBackground.setAutoDraw(True)
        
        # *pmInst1Text* updates
        if pmInst1Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pmInst1Text.frameNStart = frameN  # exact frame index
            pmInst1Text.tStart = t  # local t and not account for scr refresh
            pmInst1Text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pmInst1Text, 'tStartRefresh')  # time at next scr refresh
            pmInst1Text.setAutoDraw(True)
        
        # *PMinst1Key* updates
        waitOnFlip = False
        if PMinst1Key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            PMinst1Key.frameNStart = frameN  # exact frame index
            PMinst1Key.tStart = t  # local t and not account for scr refresh
            PMinst1Key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PMinst1Key, 'tStartRefresh')  # time at next scr refresh
            PMinst1Key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(PMinst1Key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(PMinst1Key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if PMinst1Key.status == STARTED and not waitOnFlip:
            theseKeys = PMinst1Key.getKeys(keyList=['q'], waitRelease=False)
            _PMinst1Key_allKeys.extend(theseKeys)
            if len(_PMinst1Key_allKeys):
                PMinst1Key.keys = _PMinst1Key_allKeys[-1].name  # just the last key pressed
                PMinst1Key.rt = _PMinst1Key_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PMinst1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "PMinst1" ---
    for thisComponent in PMinst1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "PMinst1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "PMinst2" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    PMinst2Key.keys = []
    PMinst2Key.rt = []
    _PMinst2Key_allKeys = []
    # keep track of which components have finished
    PMinst2Components = [PMinst2Text, PMinst2Key]
    for thisComponent in PMinst2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "PMinst2" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *PMinst2Text* updates
        if PMinst2Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            PMinst2Text.frameNStart = frameN  # exact frame index
            PMinst2Text.tStart = t  # local t and not account for scr refresh
            PMinst2Text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PMinst2Text, 'tStartRefresh')  # time at next scr refresh
            PMinst2Text.setAutoDraw(True)
        
        # *PMinst2Key* updates
        waitOnFlip = False
        if PMinst2Key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            PMinst2Key.frameNStart = frameN  # exact frame index
            PMinst2Key.tStart = t  # local t and not account for scr refresh
            PMinst2Key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PMinst2Key, 'tStartRefresh')  # time at next scr refresh
            PMinst2Key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(PMinst2Key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(PMinst2Key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if PMinst2Key.status == STARTED and not waitOnFlip:
            theseKeys = PMinst2Key.getKeys(keyList=['return'], waitRelease=False)
            _PMinst2Key_allKeys.extend(theseKeys)
            if len(_PMinst2Key_allKeys):
                PMinst2Key.keys = _PMinst2Key_allKeys[-1].name  # just the last key pressed
                PMinst2Key.rt = _PMinst2Key_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PMinst2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "PMinst2" ---
    for thisComponent in PMinst2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "PMinst2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "PMcheck" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    PMcheckKey.keys = []
    PMcheckKey.rt = []
    _PMcheckKey_allKeys = []
    # keep track of which components have finished
    PMcheckComponents = [PMcheckText, PMcheckKey]
    for thisComponent in PMcheckComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "PMcheck" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *PMcheckText* updates
        if PMcheckText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            PMcheckText.frameNStart = frameN  # exact frame index
            PMcheckText.tStart = t  # local t and not account for scr refresh
            PMcheckText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PMcheckText, 'tStartRefresh')  # time at next scr refresh
            PMcheckText.setAutoDraw(True)
        
        # *PMcheckKey* updates
        waitOnFlip = False
        if PMcheckKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            PMcheckKey.frameNStart = frameN  # exact frame index
            PMcheckKey.tStart = t  # local t and not account for scr refresh
            PMcheckKey.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PMcheckKey, 'tStartRefresh')  # time at next scr refresh
            PMcheckKey.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(PMcheckKey.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(PMcheckKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if PMcheckKey.status == STARTED and not waitOnFlip:
            theseKeys = PMcheckKey.getKeys(keyList=['y','n'], waitRelease=False)
            _PMcheckKey_allKeys.extend(theseKeys)
            if len(_PMcheckKey_allKeys):
                PMcheckKey.keys = _PMcheckKey_allKeys[-1].name  # just the last key pressed
                PMcheckKey.rt = _PMcheckKey_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PMcheckComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "PMcheck" ---
    for thisComponent in PMcheckComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from PMcheckCode
    thisExp.addData("PMunderstand", PMcheckKey.keys)
    if PMcheckKey.keys == 'y':
        PMunderstand.finished = True
    elif PMcheckKey.keys == 'Y':
        PMunderstand.finished = True
    event.clearEvents('keyboard')
    # the Routine "PMcheck" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'PMunderstand'


# --- Prepare to start Routine "PMcue" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
cueTextbox.reset()
cueNextKey.keys = []
cueNextKey.rt = []
_cueNextKey_allKeys = []
# keep track of which components have finished
PMcueComponents = [cueText, cueTextbox, cueNextKey, cueNextText]
for thisComponent in PMcueComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "PMcue" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *cueText* updates
    if cueText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        cueText.frameNStart = frameN  # exact frame index
        cueText.tStart = t  # local t and not account for scr refresh
        cueText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(cueText, 'tStartRefresh')  # time at next scr refresh
        cueText.setAutoDraw(True)
    
    # *cueTextbox* updates
    if cueTextbox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        cueTextbox.frameNStart = frameN  # exact frame index
        cueTextbox.tStart = t  # local t and not account for scr refresh
        cueTextbox.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(cueTextbox, 'tStartRefresh')  # time at next scr refresh
        cueTextbox.setAutoDraw(True)
    
    # *cueNextKey* updates
    waitOnFlip = False
    if cueNextKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        cueNextKey.frameNStart = frameN  # exact frame index
        cueNextKey.tStart = t  # local t and not account for scr refresh
        cueNextKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(cueNextKey, 'tStartRefresh')  # time at next scr refresh
        cueNextKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(cueNextKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(cueNextKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if cueNextKey.status == STARTED and not waitOnFlip:
        theseKeys = cueNextKey.getKeys(keyList=['return'], waitRelease=False)
        _cueNextKey_allKeys.extend(theseKeys)
        if len(_cueNextKey_allKeys):
            cueNextKey.keys = _cueNextKey_allKeys[-1].name  # just the last key pressed
            cueNextKey.rt = _cueNextKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *cueNextText* updates
    if cueNextText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        cueNextText.frameNStart = frameN  # exact frame index
        cueNextText.tStart = t  # local t and not account for scr refresh
        cueNextText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(cueNextText, 'tStartRefresh')  # time at next scr refresh
        cueNextText.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in PMcueComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "PMcue" ---
for thisComponent in PMcueComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('cueTextbox.text',cueTextbox.text)
# the Routine "PMcue" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "PMintention" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
intentionTextbox.reset()
intentionNextKey.keys = []
intentionNextKey.rt = []
_intentionNextKey_allKeys = []
# keep track of which components have finished
PMintentionComponents = [intentionText, intentionTextbox, intentionNextKey, intentionNextText]
for thisComponent in PMintentionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "PMintention" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *intentionText* updates
    if intentionText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intentionText.frameNStart = frameN  # exact frame index
        intentionText.tStart = t  # local t and not account for scr refresh
        intentionText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intentionText, 'tStartRefresh')  # time at next scr refresh
        intentionText.setAutoDraw(True)
    
    # *intentionTextbox* updates
    if intentionTextbox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intentionTextbox.frameNStart = frameN  # exact frame index
        intentionTextbox.tStart = t  # local t and not account for scr refresh
        intentionTextbox.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intentionTextbox, 'tStartRefresh')  # time at next scr refresh
        intentionTextbox.setAutoDraw(True)
    
    # *intentionNextKey* updates
    waitOnFlip = False
    if intentionNextKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intentionNextKey.frameNStart = frameN  # exact frame index
        intentionNextKey.tStart = t  # local t and not account for scr refresh
        intentionNextKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intentionNextKey, 'tStartRefresh')  # time at next scr refresh
        intentionNextKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(intentionNextKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(intentionNextKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if intentionNextKey.status == STARTED and not waitOnFlip:
        theseKeys = intentionNextKey.getKeys(keyList=['space'], waitRelease=False)
        _intentionNextKey_allKeys.extend(theseKeys)
        if len(_intentionNextKey_allKeys):
            intentionNextKey.keys = _intentionNextKey_allKeys[-1].name  # just the last key pressed
            intentionNextKey.rt = _intentionNextKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *intentionNextText* updates
    if intentionNextText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intentionNextText.frameNStart = frameN  # exact frame index
        intentionNextText.tStart = t  # local t and not account for scr refresh
        intentionNextText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intentionNextText, 'tStartRefresh')  # time at next scr refresh
        intentionNextText.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in PMintentionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "PMintention" ---
for thisComponent in PMintentionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('intentionTextbox.text',intentionTextbox.text)
# the Routine "PMintention" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "LDTbegin1" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
begin1Key.keys = []
begin1Key.rt = []
_begin1Key_allKeys = []
# keep track of which components have finished
LDTbegin1Components = [begin1Text, begin1Key]
for thisComponent in LDTbegin1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "LDTbegin1" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *begin1Text* updates
    if begin1Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        begin1Text.frameNStart = frameN  # exact frame index
        begin1Text.tStart = t  # local t and not account for scr refresh
        begin1Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(begin1Text, 'tStartRefresh')  # time at next scr refresh
        begin1Text.setAutoDraw(True)
    
    # *begin1Key* updates
    waitOnFlip = False
    if begin1Key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        begin1Key.frameNStart = frameN  # exact frame index
        begin1Key.tStart = t  # local t and not account for scr refresh
        begin1Key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(begin1Key, 'tStartRefresh')  # time at next scr refresh
        begin1Key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(begin1Key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(begin1Key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if begin1Key.status == STARTED and not waitOnFlip:
        theseKeys = begin1Key.getKeys(keyList=['q'], waitRelease=False)
        _begin1Key_allKeys.extend(theseKeys)
        if len(_begin1Key_allKeys):
            begin1Key.keys = _begin1Key_allKeys[-1].name  # just the last key pressed
            begin1Key.rt = _begin1Key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in LDTbegin1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "LDTbegin1" ---
for thisComponent in LDTbegin1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "LDTbegin1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "LDTbegin2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
begin2Key.keys = []
begin2Key.rt = []
_begin2Key_allKeys = []
# keep track of which components have finished
LDTbegin2Components = [begin2Text, begin2Key]
for thisComponent in LDTbegin2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "LDTbegin2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *begin2Text* updates
    if begin2Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        begin2Text.frameNStart = frameN  # exact frame index
        begin2Text.tStart = t  # local t and not account for scr refresh
        begin2Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(begin2Text, 'tStartRefresh')  # time at next scr refresh
        begin2Text.setAutoDraw(True)
    
    # *begin2Key* updates
    waitOnFlip = False
    if begin2Key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        begin2Key.frameNStart = frameN  # exact frame index
        begin2Key.tStart = t  # local t and not account for scr refresh
        begin2Key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(begin2Key, 'tStartRefresh')  # time at next scr refresh
        begin2Key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(begin2Key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(begin2Key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if begin2Key.status == STARTED and not waitOnFlip:
        theseKeys = begin2Key.getKeys(keyList=['return'], waitRelease=False)
        _begin2Key_allKeys.extend(theseKeys)
        if len(_begin2Key_allKeys):
            begin2Key.keys = _begin2Key_allKeys[-1].name  # just the last key pressed
            begin2Key.rt = _begin2Key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in LDTbegin2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "LDTbegin2" ---
for thisComponent in LDTbegin2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "LDTbegin2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "countdown" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
countdownComponents = [five, four, three, two, one]
for thisComponent in countdownComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "countdown" ---
while continueRoutine and routineTimer.getTime() < 5.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *five* updates
    if five.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        five.frameNStart = frameN  # exact frame index
        five.tStart = t  # local t and not account for scr refresh
        five.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(five, 'tStartRefresh')  # time at next scr refresh
        five.setAutoDraw(True)
    if five.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > five.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            five.tStop = t  # not accounting for scr refresh
            five.frameNStop = frameN  # exact frame index
            five.setAutoDraw(False)
    
    # *four* updates
    if four.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        four.frameNStart = frameN  # exact frame index
        four.tStart = t  # local t and not account for scr refresh
        four.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(four, 'tStartRefresh')  # time at next scr refresh
        four.setAutoDraw(True)
    if four.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > four.tStartRefresh + 1-frameTolerance:
            # keep track of stop time/frame for later
            four.tStop = t  # not accounting for scr refresh
            four.frameNStop = frameN  # exact frame index
            four.setAutoDraw(False)
    
    # *three* updates
    if three.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        three.frameNStart = frameN  # exact frame index
        three.tStart = t  # local t and not account for scr refresh
        three.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(three, 'tStartRefresh')  # time at next scr refresh
        three.setAutoDraw(True)
    if three.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > three.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            three.tStop = t  # not accounting for scr refresh
            three.frameNStop = frameN  # exact frame index
            three.setAutoDraw(False)
    
    # *two* updates
    if two.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
        # keep track of start time/frame for later
        two.frameNStart = frameN  # exact frame index
        two.tStart = t  # local t and not account for scr refresh
        two.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(two, 'tStartRefresh')  # time at next scr refresh
        two.setAutoDraw(True)
    if two.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > two.tStartRefresh + 1-frameTolerance:
            # keep track of stop time/frame for later
            two.tStop = t  # not accounting for scr refresh
            two.frameNStop = frameN  # exact frame index
            two.setAutoDraw(False)
    
    # *one* updates
    if one.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
        # keep track of start time/frame for later
        one.frameNStart = frameN  # exact frame index
        one.tStart = t  # local t and not account for scr refresh
        one.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(one, 'tStartRefresh')  # time at next scr refresh
        one.setAutoDraw(True)
    if one.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > one.tStartRefresh + 1-frameTolerance:
            # keep track of stop time/frame for later
            one.tStop = t  # not accounting for scr refresh
            one.frameNStop = frameN  # exact frame index
            one.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in countdownComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "countdown" ---
for thisComponent in countdownComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-5.000000)

# set up handler to look after randomisation of conditions etc
LDT_block = data.TrialHandler(nReps=nBlocks, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='LDT_block')
thisExp.addLoop(LDT_block)  # add the loop to the experiment
thisLDT_block = LDT_block.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLDT_block.rgb)
if thisLDT_block != None:
    for paramName in thisLDT_block:
        exec('{} = thisLDT_block[paramName]'.format(paramName))

for thisLDT_block in LDT_block:
    currentLoop = LDT_block
    # abbreviate parameter names if possible (e.g. rgb = thisLDT_block.rgb)
    if thisLDT_block != None:
        for paramName in thisLDT_block:
            exec('{} = thisLDT_block[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "block_init" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from block_setup
    blockPM = 0
    block_stim = stim[LDT_block.thisN]
    block_blockType = blockType[LDT_block.thisN]
    block_role = role[LDT_block.thisN]
    block_wordType = wordType[LDT_block.thisN]
    block_correctKey = correctKey[LDT_block.thisN]
    block_stimLocation = stimLocation[LDT_block.thisN]
    block_blockDesc = blockDesc[LDT_block.thisN]
    # keep track of which components have finished
    block_initComponents = []
    for thisComponent in block_initComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "block_init" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block_initComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "block_init" ---
    for thisComponent in block_initComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "block_init" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    LDT_trial = data.TrialHandler(nReps=ntrials, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='LDT_trial')
    thisExp.addLoop(LDT_trial)  # add the loop to the experiment
    thisLDT_trial = LDT_trial.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLDT_trial.rgb)
    if thisLDT_trial != None:
        for paramName in thisLDT_trial:
            exec('{} = thisLDT_trial[paramName]'.format(paramName))
    
    for thisLDT_trial in LDT_trial:
        currentLoop = LDT_trial
        # abbreviate parameter names if possible (e.g. rgb = thisLDT_trial.rgb)
        if thisLDT_trial != None:
            for paramName in thisLDT_trial:
                exec('{} = thisLDT_trial[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "trial_init" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from trial_code
        this_stim = block_stim[LDT_trial.thisN]
        this_blockType = block_blockType[LDT_trial.thisN]
        this_role = block_role[LDT_trial.thisN]
        this_wordType = block_wordType[LDT_trial.thisN]
        this_correctKey = block_correctKey[LDT_trial.thisN]
        this_stimLocation = block_stimLocation[LDT_trial.thisN]
        this_blockDesc = block_blockDesc[LDT_trial.thisN]
        if this_stimLocation == 'upper':
            loc = [0,0.25]
        elif this_stimLocation == 'lower':
            loc = [0,-0.25]
        
        thisExp.addData('stim', this_stim)
        thisExp.addData('block_type', this_blockType)
        thisExp.addData('role', this_role)
        thisExp.addData('word_type', this_wordType)
        thisExp.addData('corr_key', this_correctKey)
        thisExp.addData('stim_location', this_stimLocation)
        thisExp.addData('block_desc', this_blockDesc)
        # keep track of which components have finished
        trial_initComponents = []
        for thisComponent in trial_initComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trial_init" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial_initComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial_init" ---
        for thisComponent in trial_initComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "trial_init" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "LDTfix500" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        LDTfix.setPos(loc)
        # keep track of which components have finished
        LDTfix500Components = [LDTfix]
        for thisComponent in LDTfix500Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "LDTfix500" ---
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *LDTfix* updates
            if LDTfix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                LDTfix.frameNStart = frameN  # exact frame index
                LDTfix.tStart = t  # local t and not account for scr refresh
                LDTfix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(LDTfix, 'tStartRefresh')  # time at next scr refresh
                LDTfix.setAutoDraw(True)
            if LDTfix.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > LDTfix.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    LDTfix.tStop = t  # not accounting for scr refresh
                    LDTfix.frameNStop = frameN  # exact frame index
                    LDTfix.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in LDTfix500Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "LDTfix500" ---
        for thisComponent in LDTfix500Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        
        # --- Prepare to start Routine "LDT" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        LDTWord.setPos(loc)
        LDTWord.setText(this_stim)
        LDTResp.keys = []
        LDTResp.rt = []
        _LDTResp_allKeys = []
        # keep track of which components have finished
        LDTComponents = [LDTWord, LDTResp]
        for thisComponent in LDTComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "LDT" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *LDTWord* updates
            if LDTWord.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                LDTWord.frameNStart = frameN  # exact frame index
                LDTWord.tStart = t  # local t and not account for scr refresh
                LDTWord.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(LDTWord, 'tStartRefresh')  # time at next scr refresh
                LDTWord.setAutoDraw(True)
            
            # *LDTResp* updates
            waitOnFlip = False
            if LDTResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                LDTResp.frameNStart = frameN  # exact frame index
                LDTResp.tStart = t  # local t and not account for scr refresh
                LDTResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(LDTResp, 'tStartRefresh')  # time at next scr refresh
                LDTResp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(LDTResp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(LDTResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if LDTResp.status == STARTED and not waitOnFlip:
                theseKeys = LDTResp.getKeys(keyList=['g','h','q'], waitRelease=False)
                _LDTResp_allKeys.extend(theseKeys)
                if len(_LDTResp_allKeys):
                    LDTResp.keys = _LDTResp_allKeys[-1].name  # just the last key pressed
                    LDTResp.rt = _LDTResp_allKeys[-1].rt
                    # was this correct?
                    if (LDTResp.keys == str(this_correctKey)) or (LDTResp.keys == this_correctKey):
                        LDTResp.corr = 1
                    else:
                        LDTResp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in LDTComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "LDT" ---
        for thisComponent in LDTComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from pressQcode
        if LDTResp.keys == 'q' and this_role == 'target':
            thisExp.addData('pressedQ', 1)
            blockPM = 1
        elif LDTResp.keys == 'q' and this_role == 'aftertar1':
            thisExp.addData('pressedQ_late', 1)
            blockPM = 1
        elif LDTResp.keys == 'q' and this_role == 'aftertar2':
            thisExp.addData('pressedQ_late', 1)
        elif LDTResp.keys == 'q' and this_role == 'aftertar3':
            thisExp.addData('pressedQ_late', 1)
        # check responses
        if LDTResp.keys in ['', [], None]:  # No response was made
            LDTResp.keys = None
            # was no response the correct answer?!
            if str(this_correctKey).lower() == 'none':
               LDTResp.corr = 1;  # correct non-response
            else:
               LDTResp.corr = 0;  # failed to respond (incorrectly)
        # store data for LDT_trial (TrialHandler)
        LDT_trial.addData('LDTResp.keys',LDTResp.keys)
        LDT_trial.addData('LDTResp.corr', LDTResp.corr)
        if LDTResp.keys != None:  # we had a response
            LDT_trial.addData('LDTResp.rt', LDTResp.rt)
        # the Routine "LDT" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "blank500" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        blankQResp.keys = []
        blankQResp.rt = []
        _blankQResp_allKeys = []
        # keep track of which components have finished
        blank500Components = [blank, blankQResp]
        for thisComponent in blank500Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "blank500" ---
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *blank* updates
            if blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blank.frameNStart = frameN  # exact frame index
                blank.tStart = t  # local t and not account for scr refresh
                blank.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blank, 'tStartRefresh')  # time at next scr refresh
                blank.setAutoDraw(True)
            if blank.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > blank.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    blank.tStop = t  # not accounting for scr refresh
                    blank.frameNStop = frameN  # exact frame index
                    blank.setAutoDraw(False)
            
            # *blankQResp* updates
            waitOnFlip = False
            if blankQResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blankQResp.frameNStart = frameN  # exact frame index
                blankQResp.tStart = t  # local t and not account for scr refresh
                blankQResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blankQResp, 'tStartRefresh')  # time at next scr refresh
                blankQResp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(blankQResp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(blankQResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if blankQResp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > blankQResp.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    blankQResp.tStop = t  # not accounting for scr refresh
                    blankQResp.frameNStop = frameN  # exact frame index
                    blankQResp.status = FINISHED
            if blankQResp.status == STARTED and not waitOnFlip:
                theseKeys = blankQResp.getKeys(keyList=['q'], waitRelease=False)
                _blankQResp_allKeys.extend(theseKeys)
                if len(_blankQResp_allKeys):
                    blankQResp.keys = _blankQResp_allKeys[-1].name  # just the last key pressed
                    blankQResp.rt = _blankQResp_allKeys[-1].rt
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blank500Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "blank500" ---
        for thisComponent in blank500Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from pressQcodeblank
        if blankQResp.keys == 'q' and this_role == 'target':
            thisExp.addData('pressedQ', 1)
            thisExp.addData('pressedQ_blank', 1)
            blockPM = 1
        elif blankQResp.keys == 'q' and this_role == 'aftertar1':
            thisExp.addData('pressedQ_late', 1)
            blockPM = 1
        elif blankQResp.keys == 'q' and this_role == 'aftertar2':
            thisExp.addData('pressedQ_late', 1)
        elif blankQResp.keys == 'q' and this_role == 'aftertar3':
            thisExp.addData('pressedQ_late', 1)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        thisExp.nextEntry()
        
    # completed ntrials repeats of 'LDT_trial'
    
    
    # --- Prepare to start Routine "PMCheck" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from checkCode
    print(blockPM)
    if this_blockDesc == 'HiDemTar' or this_blockDesc == 'LoDemTar':
        if blockPM == 1:
            thisExp.addData('PM_accuracy', 1)
        else:
            thisExp.addData('PM_accuracy', 0)
    else:
        thisExp.addData('PM_accuracy', 'NA')
    # keep track of which components have finished
    PMCheckComponents = []
    for thisComponent in PMCheckComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "PMCheck" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PMCheckComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "PMCheck" ---
    for thisComponent in PMCheckComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "PMCheck" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "block_break" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from breakCode
    if (int(LDT_block.thisN) + 1) == nBlocks:
        continueRoutine = False
    else:
        continueRoutine = True
    # keep track of which components have finished
    block_breakComponents = [break_screen]
    for thisComponent in block_breakComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "block_break" ---
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *break_screen* updates
        if break_screen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            break_screen.frameNStart = frameN  # exact frame index
            break_screen.tStart = t  # local t and not account for scr refresh
            break_screen.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(break_screen, 'tStartRefresh')  # time at next scr refresh
            break_screen.setAutoDraw(True)
        if break_screen.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > break_screen.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                break_screen.tStop = t  # not accounting for scr refresh
                break_screen.frameNStop = frameN  # exact frame index
                break_screen.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block_breakComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "block_break" ---
    for thisComponent in block_breakComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    
    # --- Prepare to start Routine "LDTcountdown" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from countdownCode
    if (int(LDT_block.thisN) + 1) == nBlocks:
        continueRoutine = False
    else:
        continueRoutine = True
    # keep track of which components have finished
    LDTcountdownComponents = [countdown5Text, countdown4text, countdown3Text, countdown2Text, countdown1Text]
    for thisComponent in LDTcountdownComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "LDTcountdown" ---
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *countdown5Text* updates
        if countdown5Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            countdown5Text.frameNStart = frameN  # exact frame index
            countdown5Text.tStart = t  # local t and not account for scr refresh
            countdown5Text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(countdown5Text, 'tStartRefresh')  # time at next scr refresh
            countdown5Text.setAutoDraw(True)
        if countdown5Text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > countdown5Text.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                countdown5Text.tStop = t  # not accounting for scr refresh
                countdown5Text.frameNStop = frameN  # exact frame index
                countdown5Text.setAutoDraw(False)
        
        # *countdown4text* updates
        if countdown4text.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            countdown4text.frameNStart = frameN  # exact frame index
            countdown4text.tStart = t  # local t and not account for scr refresh
            countdown4text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(countdown4text, 'tStartRefresh')  # time at next scr refresh
            countdown4text.setAutoDraw(True)
        if countdown4text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > countdown4text.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                countdown4text.tStop = t  # not accounting for scr refresh
                countdown4text.frameNStop = frameN  # exact frame index
                countdown4text.setAutoDraw(False)
        
        # *countdown3Text* updates
        if countdown3Text.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            countdown3Text.frameNStart = frameN  # exact frame index
            countdown3Text.tStart = t  # local t and not account for scr refresh
            countdown3Text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(countdown3Text, 'tStartRefresh')  # time at next scr refresh
            countdown3Text.setAutoDraw(True)
        if countdown3Text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > countdown3Text.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                countdown3Text.tStop = t  # not accounting for scr refresh
                countdown3Text.frameNStop = frameN  # exact frame index
                countdown3Text.setAutoDraw(False)
        
        # *countdown2Text* updates
        if countdown2Text.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            countdown2Text.frameNStart = frameN  # exact frame index
            countdown2Text.tStart = t  # local t and not account for scr refresh
            countdown2Text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(countdown2Text, 'tStartRefresh')  # time at next scr refresh
            countdown2Text.setAutoDraw(True)
        if countdown2Text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > countdown2Text.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                countdown2Text.tStop = t  # not accounting for scr refresh
                countdown2Text.frameNStop = frameN  # exact frame index
                countdown2Text.setAutoDraw(False)
        
        # *countdown1Text* updates
        if countdown1Text.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
            # keep track of start time/frame for later
            countdown1Text.frameNStart = frameN  # exact frame index
            countdown1Text.tStart = t  # local t and not account for scr refresh
            countdown1Text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(countdown1Text, 'tStartRefresh')  # time at next scr refresh
            countdown1Text.setAutoDraw(True)
        if countdown1Text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > countdown1Text.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                countdown1Text.tStop = t  # not accounting for scr refresh
                countdown1Text.frameNStop = frameN  # exact frame index
                countdown1Text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in LDTcountdownComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "LDTcountdown" ---
    for thisComponent in LDTcountdownComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    thisExp.nextEntry()
    
# completed nBlocks repeats of 'LDT_block'


# --- Prepare to start Routine "postExpInst" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
postInstKey.keys = []
postInstKey.rt = []
_postInstKey_allKeys = []
# keep track of which components have finished
postExpInstComponents = [postInstText, postInstKey]
for thisComponent in postExpInstComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "postExpInst" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *postInstText* updates
    if postInstText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        postInstText.frameNStart = frameN  # exact frame index
        postInstText.tStart = t  # local t and not account for scr refresh
        postInstText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(postInstText, 'tStartRefresh')  # time at next scr refresh
        postInstText.setAutoDraw(True)
    
    # *postInstKey* updates
    waitOnFlip = False
    if postInstKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        postInstKey.frameNStart = frameN  # exact frame index
        postInstKey.tStart = t  # local t and not account for scr refresh
        postInstKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(postInstKey, 'tStartRefresh')  # time at next scr refresh
        postInstKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(postInstKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(postInstKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if postInstKey.status == STARTED and not waitOnFlip:
        theseKeys = postInstKey.getKeys(keyList=['return'], waitRelease=False)
        _postInstKey_allKeys.extend(theseKeys)
        if len(_postInstKey_allKeys):
            postInstKey.keys = _postInstKey_allKeys[-1].name  # just the last key pressed
            postInstKey.rt = _postInstKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in postExpInstComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "postExpInst" ---
for thisComponent in postExpInstComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "postExpInst" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "postExpQ1" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
Q1Key.keys = []
Q1Key.rt = []
_Q1Key_allKeys = []
# keep track of which components have finished
postExpQ1Components = [Q1Text, Q1Key]
for thisComponent in postExpQ1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "postExpQ1" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Q1Text* updates
    if Q1Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q1Text.frameNStart = frameN  # exact frame index
        Q1Text.tStart = t  # local t and not account for scr refresh
        Q1Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q1Text, 'tStartRefresh')  # time at next scr refresh
        Q1Text.setAutoDraw(True)
    
    # *Q1Key* updates
    waitOnFlip = False
    if Q1Key.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        Q1Key.frameNStart = frameN  # exact frame index
        Q1Key.tStart = t  # local t and not account for scr refresh
        Q1Key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q1Key, 'tStartRefresh')  # time at next scr refresh
        Q1Key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Q1Key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Q1Key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Q1Key.status == STARTED and not waitOnFlip:
        theseKeys = Q1Key.getKeys(keyList=['y','n'], waitRelease=False)
        _Q1Key_allKeys.extend(theseKeys)
        if len(_Q1Key_allKeys):
            Q1Key.keys = _Q1Key_allKeys[-1].name  # just the last key pressed
            Q1Key.rt = _Q1Key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in postExpQ1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "postExpQ1" ---
for thisComponent in postExpQ1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from Q1Code
thisExp.addData("postQ1", Q1Key.keys)

event.clearEvents('keyboard')
# the Routine "postExpQ1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "postExpQ2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
Q2Textbox.reset()
Q2Key.keys = []
Q2Key.rt = []
_Q2Key_allKeys = []
# keep track of which components have finished
postExpQ2Components = [Q2Text, Q2Textbox, Q2Next, Q2Key]
for thisComponent in postExpQ2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "postExpQ2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Q2Text* updates
    if Q2Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q2Text.frameNStart = frameN  # exact frame index
        Q2Text.tStart = t  # local t and not account for scr refresh
        Q2Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q2Text, 'tStartRefresh')  # time at next scr refresh
        Q2Text.setAutoDraw(True)
    
    # *Q2Textbox* updates
    if Q2Textbox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q2Textbox.frameNStart = frameN  # exact frame index
        Q2Textbox.tStart = t  # local t and not account for scr refresh
        Q2Textbox.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q2Textbox, 'tStartRefresh')  # time at next scr refresh
        Q2Textbox.setAutoDraw(True)
    
    # *Q2Next* updates
    if Q2Next.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q2Next.frameNStart = frameN  # exact frame index
        Q2Next.tStart = t  # local t and not account for scr refresh
        Q2Next.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q2Next, 'tStartRefresh')  # time at next scr refresh
        Q2Next.setAutoDraw(True)
    
    # *Q2Key* updates
    waitOnFlip = False
    if Q2Key.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        Q2Key.frameNStart = frameN  # exact frame index
        Q2Key.tStart = t  # local t and not account for scr refresh
        Q2Key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q2Key, 'tStartRefresh')  # time at next scr refresh
        Q2Key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Q2Key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Q2Key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Q2Key.status == STARTED and not waitOnFlip:
        theseKeys = Q2Key.getKeys(keyList=['return'], waitRelease=False)
        _Q2Key_allKeys.extend(theseKeys)
        if len(_Q2Key_allKeys):
            Q2Key.keys = _Q2Key_allKeys[-1].name  # just the last key pressed
            Q2Key.rt = _Q2Key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in postExpQ2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "postExpQ2" ---
for thisComponent in postExpQ2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Q2Textbox.text',Q2Textbox.text)
# the Routine "postExpQ2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "postExpQ3" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
Q3Textbox.reset()
Q3Key.keys = []
Q3Key.rt = []
_Q3Key_allKeys = []
# keep track of which components have finished
postExpQ3Components = [Q3Text, Q3Textbox, Q3Next, Q3Key]
for thisComponent in postExpQ3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "postExpQ3" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Q3Text* updates
    if Q3Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q3Text.frameNStart = frameN  # exact frame index
        Q3Text.tStart = t  # local t and not account for scr refresh
        Q3Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q3Text, 'tStartRefresh')  # time at next scr refresh
        Q3Text.setAutoDraw(True)
    
    # *Q3Textbox* updates
    if Q3Textbox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q3Textbox.frameNStart = frameN  # exact frame index
        Q3Textbox.tStart = t  # local t and not account for scr refresh
        Q3Textbox.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q3Textbox, 'tStartRefresh')  # time at next scr refresh
        Q3Textbox.setAutoDraw(True)
    
    # *Q3Next* updates
    if Q3Next.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q3Next.frameNStart = frameN  # exact frame index
        Q3Next.tStart = t  # local t and not account for scr refresh
        Q3Next.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q3Next, 'tStartRefresh')  # time at next scr refresh
        Q3Next.setAutoDraw(True)
    
    # *Q3Key* updates
    waitOnFlip = False
    if Q3Key.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        Q3Key.frameNStart = frameN  # exact frame index
        Q3Key.tStart = t  # local t and not account for scr refresh
        Q3Key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q3Key, 'tStartRefresh')  # time at next scr refresh
        Q3Key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Q3Key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Q3Key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Q3Key.status == STARTED and not waitOnFlip:
        theseKeys = Q3Key.getKeys(keyList=['space'], waitRelease=False)
        _Q3Key_allKeys.extend(theseKeys)
        if len(_Q3Key_allKeys):
            Q3Key.keys = _Q3Key_allKeys[-1].name  # just the last key pressed
            Q3Key.rt = _Q3Key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in postExpQ3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "postExpQ3" ---
for thisComponent in postExpQ3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Q3Textbox.text',Q3Textbox.text)
# the Routine "postExpQ3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "postExpQ4" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
Q4Key.keys = []
Q4Key.rt = []
_Q4Key_allKeys = []
# keep track of which components have finished
postExpQ4Components = [Q4Text, Q4Key]
for thisComponent in postExpQ4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "postExpQ4" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Q4Text* updates
    if Q4Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q4Text.frameNStart = frameN  # exact frame index
        Q4Text.tStart = t  # local t and not account for scr refresh
        Q4Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q4Text, 'tStartRefresh')  # time at next scr refresh
        Q4Text.setAutoDraw(True)
    
    # *Q4Key* updates
    waitOnFlip = False
    if Q4Key.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        Q4Key.frameNStart = frameN  # exact frame index
        Q4Key.tStart = t  # local t and not account for scr refresh
        Q4Key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q4Key, 'tStartRefresh')  # time at next scr refresh
        Q4Key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Q4Key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Q4Key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Q4Key.status == STARTED and not waitOnFlip:
        theseKeys = Q4Key.getKeys(keyList=['0','1','2','3','4'], waitRelease=False)
        _Q4Key_allKeys.extend(theseKeys)
        if len(_Q4Key_allKeys):
            Q4Key.keys = _Q4Key_allKeys[-1].name  # just the last key pressed
            Q4Key.rt = _Q4Key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in postExpQ4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "postExpQ4" ---
for thisComponent in postExpQ4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from Q4code
thisExp.addData("Q4", Q4Key.keys.replace('num_', ''))
# the Routine "postExpQ4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "posExpQ5" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
Q5Key.keys = []
Q5Key.rt = []
_Q5Key_allKeys = []
# keep track of which components have finished
posExpQ5Components = [Q5Text, Q5Key]
for thisComponent in posExpQ5Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "posExpQ5" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Q5Text* updates
    if Q5Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q5Text.frameNStart = frameN  # exact frame index
        Q5Text.tStart = t  # local t and not account for scr refresh
        Q5Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q5Text, 'tStartRefresh')  # time at next scr refresh
        Q5Text.setAutoDraw(True)
    
    # *Q5Key* updates
    waitOnFlip = False
    if Q5Key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q5Key.frameNStart = frameN  # exact frame index
        Q5Key.tStart = t  # local t and not account for scr refresh
        Q5Key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q5Key, 'tStartRefresh')  # time at next scr refresh
        Q5Key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Q5Key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Q5Key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Q5Key.status == STARTED and not waitOnFlip:
        theseKeys = Q5Key.getKeys(keyList=['1','2','3','4'], waitRelease=False)
        _Q5Key_allKeys.extend(theseKeys)
        if len(_Q5Key_allKeys):
            Q5Key.keys = _Q5Key_allKeys[-1].name  # just the last key pressed
            Q5Key.rt = _Q5Key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in posExpQ5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "posExpQ5" ---
for thisComponent in posExpQ5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from Q5code
thisExp.addData("Q5", Q5Key.keys.replace('num_', ''))
# the Routine "posExpQ5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "postExpQ6" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
Q6Key.keys = []
Q6Key.rt = []
_Q6Key_allKeys = []
# keep track of which components have finished
postExpQ6Components = [Q6Text, Q6Key]
for thisComponent in postExpQ6Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "postExpQ6" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Q6Text* updates
    if Q6Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q6Text.frameNStart = frameN  # exact frame index
        Q6Text.tStart = t  # local t and not account for scr refresh
        Q6Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q6Text, 'tStartRefresh')  # time at next scr refresh
        Q6Text.setAutoDraw(True)
    
    # *Q6Key* updates
    waitOnFlip = False
    if Q6Key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q6Key.frameNStart = frameN  # exact frame index
        Q6Key.tStart = t  # local t and not account for scr refresh
        Q6Key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q6Key, 'tStartRefresh')  # time at next scr refresh
        Q6Key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Q6Key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Q6Key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Q6Key.status == STARTED and not waitOnFlip:
        theseKeys = Q6Key.getKeys(keyList=['y','n'], waitRelease=False)
        _Q6Key_allKeys.extend(theseKeys)
        if len(_Q6Key_allKeys):
            Q6Key.keys = _Q6Key_allKeys[-1].name  # just the last key pressed
            Q6Key.rt = _Q6Key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in postExpQ6Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "postExpQ6" ---
for thisComponent in postExpQ6Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if Q6Key.keys in ['', [], None]:  # No response was made
    Q6Key.keys = None
thisExp.addData('Q6Key.keys',Q6Key.keys)
if Q6Key.keys != None:  # we had a response
    thisExp.addData('Q6Key.rt', Q6Key.rt)
thisExp.nextEntry()
# the Routine "postExpQ6" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "postExpQ7" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from Q7Code
if Q6Key.keys == 'n':
    continueRoutine = False
Q7Key.keys = []
Q7Key.rt = []
_Q7Key_allKeys = []
# keep track of which components have finished
postExpQ7Components = [Q7Text, Q7Key]
for thisComponent in postExpQ7Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "postExpQ7" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Q7Text* updates
    if Q7Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q7Text.frameNStart = frameN  # exact frame index
        Q7Text.tStart = t  # local t and not account for scr refresh
        Q7Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q7Text, 'tStartRefresh')  # time at next scr refresh
        Q7Text.setAutoDraw(True)
    
    # *Q7Key* updates
    waitOnFlip = False
    if Q7Key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q7Key.frameNStart = frameN  # exact frame index
        Q7Key.tStart = t  # local t and not account for scr refresh
        Q7Key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q7Key, 'tStartRefresh')  # time at next scr refresh
        Q7Key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Q7Key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Q7Key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Q7Key.status == STARTED and not waitOnFlip:
        theseKeys = Q7Key.getKeys(keyList=['u','l','x'], waitRelease=False)
        _Q7Key_allKeys.extend(theseKeys)
        if len(_Q7Key_allKeys):
            Q7Key.keys = _Q7Key_allKeys[-1].name  # just the last key pressed
            Q7Key.rt = _Q7Key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in postExpQ7Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "postExpQ7" ---
for thisComponent in postExpQ7Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from Q7Code
if hDemandLoc == 'upper' and Q7Key.keys == 'u':
    thisExp.addData('postQ7_correct', 1)
elif hDemandLoc == 'lower' and Q7Key.keys == 'l':
    thisExp.addData('postQ7_correct', 1)
else:
    thisExp.addData('postQ7_correct', 0)

thisExp.addData("postQ7", Q7Key.keys)
# the Routine "postExpQ7" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "postExpQ8" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
Q8Textbox.reset()
Q8Key.keys = []
Q8Key.rt = []
_Q8Key_allKeys = []
# keep track of which components have finished
postExpQ8Components = [Q8Text, Q8Textbox, Q8Next, Q8Key]
for thisComponent in postExpQ8Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "postExpQ8" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Q8Text* updates
    if Q8Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q8Text.frameNStart = frameN  # exact frame index
        Q8Text.tStart = t  # local t and not account for scr refresh
        Q8Text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q8Text, 'tStartRefresh')  # time at next scr refresh
        Q8Text.setAutoDraw(True)
    
    # *Q8Textbox* updates
    if Q8Textbox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q8Textbox.frameNStart = frameN  # exact frame index
        Q8Textbox.tStart = t  # local t and not account for scr refresh
        Q8Textbox.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q8Textbox, 'tStartRefresh')  # time at next scr refresh
        Q8Textbox.setAutoDraw(True)
    
    # *Q8Next* updates
    if Q8Next.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Q8Next.frameNStart = frameN  # exact frame index
        Q8Next.tStart = t  # local t and not account for scr refresh
        Q8Next.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q8Next, 'tStartRefresh')  # time at next scr refresh
        Q8Next.setAutoDraw(True)
    
    # *Q8Key* updates
    waitOnFlip = False
    if Q8Key.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        Q8Key.frameNStart = frameN  # exact frame index
        Q8Key.tStart = t  # local t and not account for scr refresh
        Q8Key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Q8Key, 'tStartRefresh')  # time at next scr refresh
        Q8Key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Q8Key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Q8Key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Q8Key.status == STARTED and not waitOnFlip:
        theseKeys = Q8Key.getKeys(keyList=['space'], waitRelease=False)
        _Q8Key_allKeys.extend(theseKeys)
        if len(_Q8Key_allKeys):
            Q8Key.keys = _Q8Key_allKeys[-1].name  # just the last key pressed
            Q8Key.rt = _Q8Key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in postExpQ8Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "postExpQ8" ---
for thisComponent in postExpQ8Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Q8Textbox.text',Q8Textbox.text)
# the Routine "postExpQ8" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "demoInst" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
formInstKey.keys = []
formInstKey.rt = []
_formInstKey_allKeys = []
# keep track of which components have finished
demoInstComponents = [formInstText, formInstKey]
for thisComponent in demoInstComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "demoInst" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *formInstText* updates
    if formInstText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        formInstText.frameNStart = frameN  # exact frame index
        formInstText.tStart = t  # local t and not account for scr refresh
        formInstText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(formInstText, 'tStartRefresh')  # time at next scr refresh
        formInstText.setAutoDraw(True)
    
    # *formInstKey* updates
    waitOnFlip = False
    if formInstKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        formInstKey.frameNStart = frameN  # exact frame index
        formInstKey.tStart = t  # local t and not account for scr refresh
        formInstKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(formInstKey, 'tStartRefresh')  # time at next scr refresh
        formInstKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(formInstKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(formInstKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if formInstKey.status == STARTED and not waitOnFlip:
        theseKeys = formInstKey.getKeys(keyList=['space'], waitRelease=False)
        _formInstKey_allKeys.extend(theseKeys)
        if len(_formInstKey_allKeys):
            formInstKey.keys = _formInstKey_allKeys[-1].name  # just the last key pressed
            formInstKey.rt = _formInstKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in demoInstComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "demoInst" ---
for thisComponent in demoInstComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "demoInst" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "demoEducation" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
education.keys = []
education.rt = []
_education_allKeys = []
# keep track of which components have finished
demoEducationComponents = [eduText, education]
for thisComponent in demoEducationComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "demoEducation" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *eduText* updates
    if eduText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        eduText.frameNStart = frameN  # exact frame index
        eduText.tStart = t  # local t and not account for scr refresh
        eduText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(eduText, 'tStartRefresh')  # time at next scr refresh
        eduText.setAutoDraw(True)
    
    # *education* updates
    waitOnFlip = False
    if education.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        education.frameNStart = frameN  # exact frame index
        education.tStart = t  # local t and not account for scr refresh
        education.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(education, 'tStartRefresh')  # time at next scr refresh
        education.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(education.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(education.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if education.status == STARTED and not waitOnFlip:
        theseKeys = education.getKeys(keyList=['1','2','3','4','5','6','7'], waitRelease=False)
        _education_allKeys.extend(theseKeys)
        if len(_education_allKeys):
            education.keys = _education_allKeys[-1].name  # just the last key pressed
            education.rt = _education_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in demoEducationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "demoEducation" ---
for thisComponent in demoEducationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from eduCode
thisExp.addData("education", education.keys.replace('num_', ''))
# the Routine "demoEducation" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "demoMedication" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
medTextbox.reset()
medNextKey.keys = []
medNextKey.rt = []
_medNextKey_allKeys = []
# keep track of which components have finished
demoMedicationComponents = [medText, medTextbox, medNextText, medNextKey]
for thisComponent in demoMedicationComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "demoMedication" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *medText* updates
    if medText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        medText.frameNStart = frameN  # exact frame index
        medText.tStart = t  # local t and not account for scr refresh
        medText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(medText, 'tStartRefresh')  # time at next scr refresh
        medText.setAutoDraw(True)
    
    # *medTextbox* updates
    if medTextbox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        medTextbox.frameNStart = frameN  # exact frame index
        medTextbox.tStart = t  # local t and not account for scr refresh
        medTextbox.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(medTextbox, 'tStartRefresh')  # time at next scr refresh
        medTextbox.setAutoDraw(True)
    
    # *medNextText* updates
    if medNextText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        medNextText.frameNStart = frameN  # exact frame index
        medNextText.tStart = t  # local t and not account for scr refresh
        medNextText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(medNextText, 'tStartRefresh')  # time at next scr refresh
        medNextText.setAutoDraw(True)
    
    # *medNextKey* updates
    waitOnFlip = False
    if medNextKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        medNextKey.frameNStart = frameN  # exact frame index
        medNextKey.tStart = t  # local t and not account for scr refresh
        medNextKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(medNextKey, 'tStartRefresh')  # time at next scr refresh
        medNextKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(medNextKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(medNextKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if medNextKey.status == STARTED and not waitOnFlip:
        theseKeys = medNextKey.getKeys(keyList=['return'], waitRelease=False)
        _medNextKey_allKeys.extend(theseKeys)
        if len(_medNextKey_allKeys):
            medNextKey.keys = _medNextKey_allKeys[-1].name  # just the last key pressed
            medNextKey.rt = _medNextKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in demoMedicationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "demoMedication" ---
for thisComponent in demoMedicationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('medTextbox.text',medTextbox.text)
# the Routine "demoMedication" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "demoHealth" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
health.keys = []
health.rt = []
_health_allKeys = []
# keep track of which components have finished
demoHealthComponents = [healthText, health]
for thisComponent in demoHealthComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "demoHealth" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *healthText* updates
    if healthText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        healthText.frameNStart = frameN  # exact frame index
        healthText.tStart = t  # local t and not account for scr refresh
        healthText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(healthText, 'tStartRefresh')  # time at next scr refresh
        healthText.setAutoDraw(True)
    
    # *health* updates
    waitOnFlip = False
    if health.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        health.frameNStart = frameN  # exact frame index
        health.tStart = t  # local t and not account for scr refresh
        health.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(health, 'tStartRefresh')  # time at next scr refresh
        health.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(health.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(health.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if health.status == STARTED and not waitOnFlip:
        theseKeys = health.getKeys(keyList=['1','2','3','4','5','6'], waitRelease=False)
        _health_allKeys.extend(theseKeys)
        if len(_health_allKeys):
            health.keys = _health_allKeys[-1].name  # just the last key pressed
            health.rt = _health_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in demoHealthComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "demoHealth" ---
for thisComponent in demoHealthComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from healthCode
thisExp.addData("health", health.keys.replace('num_', ''))

# the Routine "demoHealth" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "demoHealthLimit" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
healthLimit.keys = []
healthLimit.rt = []
_healthLimit_allKeys = []
# keep track of which components have finished
demoHealthLimitComponents = [healthLimitText, healthLimit]
for thisComponent in demoHealthLimitComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "demoHealthLimit" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *healthLimitText* updates
    if healthLimitText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        healthLimitText.frameNStart = frameN  # exact frame index
        healthLimitText.tStart = t  # local t and not account for scr refresh
        healthLimitText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(healthLimitText, 'tStartRefresh')  # time at next scr refresh
        healthLimitText.setAutoDraw(True)
    
    # *healthLimit* updates
    waitOnFlip = False
    if healthLimit.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        healthLimit.frameNStart = frameN  # exact frame index
        healthLimit.tStart = t  # local t and not account for scr refresh
        healthLimit.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(healthLimit, 'tStartRefresh')  # time at next scr refresh
        healthLimit.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(healthLimit.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(healthLimit.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if healthLimit.status == STARTED and not waitOnFlip:
        theseKeys = healthLimit.getKeys(keyList=['1','2','3','4','5'], waitRelease=False)
        _healthLimit_allKeys.extend(theseKeys)
        if len(_healthLimit_allKeys):
            healthLimit.keys = _healthLimit_allKeys[-1].name  # just the last key pressed
            healthLimit.rt = _healthLimit_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in demoHealthLimitComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "demoHealthLimit" ---
for thisComponent in demoHealthLimitComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from healthLimitCode
thisExp.addData("healthLimit", healthLimit.keys.replace('num_', ''))

# the Routine "demoHealthLimit" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "demoPsych" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
psychKey.keys = []
psychKey.rt = []
_psychKey_allKeys = []
# keep track of which components have finished
demoPsychComponents = [psychText, psychKey]
for thisComponent in demoPsychComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "demoPsych" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *psychText* updates
    if psychText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        psychText.frameNStart = frameN  # exact frame index
        psychText.tStart = t  # local t and not account for scr refresh
        psychText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(psychText, 'tStartRefresh')  # time at next scr refresh
        psychText.setAutoDraw(True)
    
    # *psychKey* updates
    waitOnFlip = False
    if psychKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        psychKey.frameNStart = frameN  # exact frame index
        psychKey.tStart = t  # local t and not account for scr refresh
        psychKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(psychKey, 'tStartRefresh')  # time at next scr refresh
        psychKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(psychKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(psychKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if psychKey.status == STARTED and not waitOnFlip:
        theseKeys = psychKey.getKeys(keyList=['1','2','3','4','5','6','7'], waitRelease=False)
        _psychKey_allKeys.extend(theseKeys)
        if len(_psychKey_allKeys):
            psychKey.keys = _psychKey_allKeys[-1].name  # just the last key pressed
            psychKey.rt = _psychKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in demoPsychComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "demoPsych" ---
for thisComponent in demoPsychComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from psychCode
thisExp.addData("psych", psychKey.keys.replace('num_', ''))

# the Routine "demoPsych" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "finish" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
finishComponents = [finishText]
for thisComponent in finishComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "finish" ---
while continueRoutine and routineTimer.getTime() < 5.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *finishText* updates
    if finishText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        finishText.frameNStart = frameN  # exact frame index
        finishText.tStart = t  # local t and not account for scr refresh
        finishText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(finishText, 'tStartRefresh')  # time at next scr refresh
        finishText.setAutoDraw(True)
    if finishText.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > finishText.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            finishText.tStop = t  # not accounting for scr refresh
            finishText.frameNStop = frameN  # exact frame index
            finishText.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in finishComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "finish" ---
for thisComponent in finishComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-5.000000)

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
