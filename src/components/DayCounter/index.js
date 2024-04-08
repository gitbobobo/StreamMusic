
export default function DayCounter({dateStr}) {
    // 计算当前日期与传入的日期之间的天数
    const date1 = new Date();
    const date2 = new Date(dateStr);
    const diffTime = Math.abs(date2 - date1);
    const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));

  return (
    <span>{diffDays}</span>
  );
}
