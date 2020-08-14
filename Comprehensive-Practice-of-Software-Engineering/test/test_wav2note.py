import pytest
import wav2note
import numpy as np

def test_load():
    res=wav2note.loadFile('123',None)
    assert res==False
    res=wav2note.loadFile('123.wav',None)
    assert res==False
    res=wav2note.loadFile('123.wav',12.12)
    assert res==False
    
def test_music2note():
    res=wav2note.music2note([1,2,3],0)
    assert res==False
    res=wav2note.music2note(np.array([12]),12.0)
    assert res==False
    res=wav2note.music2note(np.array([[12],[12]]),None)
    assert res==False
    res=wav2note.music2note(None,0)
    assert res==False

def test_getNoteAndNum():
    res=wav2note.getNoteAndNum((1,2,3))
    assert res==False

def test_Normlize():
    res=wav2note.Normlize((1,2,3),(1,2,3))
    assert res==False
    res=wav2note.Normlize([1,2,3],(1,2,3))
    assert res==False
    res=wav2note.Normlize((1,2,3),[1,2,3])
    assert res==False

if __name__=='__main__':
    test_load()
    test_music2note()
    test_getNoteAndNum()
    test_Normlize()
