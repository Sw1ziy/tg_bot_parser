from exchanges.mexc.balance import get_balance as mexc_balance
from exchanges.bybit.balance import get_balance as bybit_balance
from exchanges.bitget.balance import get_balance as bitget_balance
from exchanges.ourbit.balance import get_balance as ourbit_balance
from exchanges.gate.balance import get_balance as gate_balance

EXCHANGES = {
    "mexc": {"title": "MEXC", "get_balance": mexc_balance},
    "bybit": {"title": "Bybit", "get_balance": bybit_balance},
    "bitget": {"title": "Bitget", "get_balance": bitget_balance},
    "ourbit": {"title": "OurBit", "get_balance": ourbit_balance},
    "gate": {"title": "Gate", "get_balance": gate_balance},
}
