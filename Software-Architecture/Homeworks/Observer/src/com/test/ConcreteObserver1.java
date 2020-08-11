package com.test;

public class ConcreteObserver1 implements Observer {

	@Override
	public void update(String s) {
		System.out.println("我是观察者1，我醒了");

	}

}
