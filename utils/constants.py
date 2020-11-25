# 登录后存储在session中的id
LOGIN_SESSION_ID = 'user_id'

"""
客户等级分类
"""
RANK_NORMAL = 1
RANK_COMMONLY = 2
RANK_ORDINARY = 3
RANK_ITEMS = (
    (RANK_NORMAL, '重点客户'),
    (RANK_COMMONLY, '一般客户'),
    (RANK_ORDINARY, '普通客户'),
)

"""
客户规模
"""
SCALE_TEN = 11
SCALE_FIF = 22
SCALE_HUN = 33
SCALE_THO = 44
SCALE_MORE = 55
SCALE_ITEMS = (
    (SCALE_TEN, '0~10人'),
    (SCALE_FIF, '10~50人'),
    (SCALE_HUN, '50~100人'),
    (SCALE_THO, '100~1000人'),
    (SCALE_MORE, '1000人及以上')
)

"""
联系人是否在职
"""
INJOB_YES = 1
INJOB_NO = 0
INJOB_ITEMS = (
    (INJOB_YES, '在职'),
    (INJOB_NO, '离职'),
)

"""
联系人职称
"""
JOB_BUSINESS = 11
JOB_MANAGER = 12
JOB_PURCHASE = 13
JOB_TECHNOLOGY = 14
JOB_AFTERSALE = 15
JOB_OTHER = 16
JOB_ITEMS = (
    (JOB_MANAGER, '经理'),
    (JOB_PURCHASE, '采购'),
    (JOB_TECHNOLOGY, '技术'),
    (JOB_AFTERSALE, '售后'),
    (JOB_BUSINESS, '业务'),
    (JOB_OTHER, '其他'),
)

"""
赢单率
"""
WINNING_NONE = 20
WINNING_ERSHI = 21
WINNING_WUSHI = 22
WINNING_BASHI = 23
WINNING_DONE = 24
WINNING_ITEMS = (
    (WINNING_NONE, '0%'),
    (WINNING_ERSHI, '20%'),
    (WINNING_WUSHI, '50%'),
    (WINNING_BASHI, '80%'),
    (WINNING_DONE, '100%')
)

"""
权限
"""
ROLE_YW = 1
ROLE_ZG = 2
ROLE_SW = 3
ROLE_JL = 4
ROLE_RS = 5
USER_ROLE = (
    (ROLE_YW, '业务'),
    (ROLE_ZG, '主管'),
    (ROLE_SW, '商务'),
    (ROLE_JL, '经理'),
    (ROLE_RS, '人事'),
)
