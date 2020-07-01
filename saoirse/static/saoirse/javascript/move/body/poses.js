var movementObject = {
    'bool': false,
    'startCount': 0,
    'mult': 0,
    'sin': [],
    'sinLength': 0,
    'callback': function(){},
    'now': {},
    'base': {},//abs coordinates on enter with no movement
    'movement': {}, // how much movement to be done
    'abs': {},//all abs 
    'rel': {
        'blank': {
            'name': 'blank',
            'symmetry': 'B',
            'AUs': {
                'AU1': {
                    'head': [[0, 0, 0], [0, 0, 0]],
                    'neck': [[0, 0, 0], [0, 0, 0]],
                },
                'AU1b': {
                    'spineLower': [[0, 0, 0], [0, 0, 0]],
                    'spineUpper': [[0, 0, 0], [0, 0, 0]],
                    'spineUpperInner': [[0, 0, 0], [0, 0, 0]],
                },
                'AU2': {
                    'shoulder': [[0, 0, 0], [0, 0, 0]],
                },
                'AU2b': {
                    'upperArm.L': [[0, 0, 0], [0, 0, 0]],
                    'upperArm.R': [[0, 0, 0], [0, 0, 0]],
                    'lowerArm.L': [[0, 0, 0], [0, 0, 0]],
                    'lowerArm.R': [[0, 0, 0], [0, 0, 0]],
                    'hand.L': [[0, 0, 0], [0, 0, 0]],
                    'hand.R': [[0, 0, 0], [0, 0, 0]],
                },
            },
            'sacc': [[0,0,0],[0,0,0]],
        },

        'rotateLeft': {
            'name': 'rotateLeft',
            'symmetry': 'B',
            'AUs': {
                'AU1': {
                    'head': [[0, 0, 0], [0, 0.4, 0]],
                    'neck': [[0, 0, 0], [0, 0.2, 0]],
                },
                'AU1b': {
                    'spineLower': [[0, 0, 0], [0, 0, 0]],
                    'spineUpper': [[0, 0, 0], [0, 0.2, 0]],
                    'spineUpperInner': [[0, 0, 0], [0, 0, 0]],
                },
                'AU2': {
                    'shoulder': [[0, 0, 0], [0, 0, 0]],
                },
                'AU2b': {
                    'upperArm.L': [[0, 0, 0], [0, 0, 0]],
                    'upperArm.R': [[0, 0, 0], [0, 0, 0]],
                    'lowerArm.L': [[0, 0, 0], [0, 0, 0]],
                    'lowerArm.R': [[0, 0, 0], [0, 0, 0]],
                    'hand.L': [[0, 0, 0], [0, 0, 0]],
                    'hand.R': [[0, 0, 0], [0, 0, 0]],
                },
            },
            'sacc': [[0,0,0],[0,-0.5,0]],
        },

        'leanBack': {
            'name': 'leanBack',
            'symmetry': 'B',
            'AUs': {
                'AU1': {
                    'head': [[0, 0, 0], [-0.1, 0, 0]],
                    'neck': [[0, 0, 0], [-0.1, 0, 0]],
                },
                'AU1b': {
                    'spineLower': [[0, 0, 0], [0, 0, 0]],
                    'spineUpper': [[0, 0, 0], [0, 0, 0]],
                    'spineUpperInner': [[0, 0, 0], [0.3, 0, 0]],
                },
                'AU2': {
                    'shoulder': [[0, 0, 0], [0, 0, 0]],
                },
                'AU2b': {
                    'upperArm.L': [[0, 0, 0], [0, 0, 0]],
                    'upperArm.R': [[0, 0, 0], [0, 0, 0]],
                    'lowerArm.L': [[0, 0, 0], [0, 0, 0]],
                    'lowerArm.R': [[0, 0, 0], [0, 0, 0]],
                    'hand.L': [[0, 0, 0], [0, 0, 0]],
                    'hand.R': [[0, 0, 0], [0, 0, 0]],
                },
            },
            'sacc': [[0,0,0],[-0.1,0,0]],
        },

        'tiltLeft': {
            'name': 'tiltLeft',
            'symmetry': 'B',
            'AUs': {
                'AU1': {
                    'head': [[0, 0, 0], [0, 0, -0.1]],
                    'neck': [[0, 0, 0], [0, 0, -0.05]],
                },
                'AU1b': {
                    'spineLower': [[0, 0, 0], [0, 0, 0]],
                    'spineUpper': [[0, 0, 0], [0, 0, 0]],
                    'spineUpperInner': [[0, 0, 0], [0, 0, -0.1]],
                },
                'AU2': {
                    'shoulder': [[0, 0, 0], [0, 0, 0]],
                },
                'AU2b': {
                    'upperArm.L': [[0, 0, 0], [0, 0, 0]],
                    'upperArm.R': [[0, 0, 0], [0, 0, 0]],
                    'lowerArm.L': [[0, 0, 0], [0, 0, 0]],
                    'lowerArm.R': [[0, 0, 0], [0, 0, 0]],
                    'hand.L': [[0, 0, 0], [0, 0, 0]],
                    'hand.R': [[0, 0, 0], [0, 0, 0]],
                },
            },
            'sacc': [[0,0,0],[0,-0.075,0]],
        },

    },

}

