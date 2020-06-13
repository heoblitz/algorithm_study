class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        var hashDict: [Int: Int] = [:]
        
        for (index, num) in nums.enumerated() {
            if let answer = hashDict[target - num] {
                if index > answer {
                    return [answer, index]
                }
                return [index, answer]
            }
            
            hashDict[num] = index
        }
        
        return [0]
    }
}
